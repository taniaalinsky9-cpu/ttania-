
import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #EBCDD2;
    }
    .stApp p, .stApp li {
        font-size: 17px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    '<h2 style="display: inline; background-color: rgba(34, 197, 94, 0.4); padding: 2px 8px; border-radius: 25px;">My Skills & Expertise</span></h2>', 
    unsafe_allow_html=True
)

st.set_page_config(page_title="Skills", page_icon="🌟", layout="wide")

st.divider()
SKILLS = [
    ("🎨", "Visual Curation & Feed Styling", 85, "#E1306C", "Menyusun tampilan visual yang konsisten dan estetik untuk feed media sosial."),
    ("🗣️", "Advanced English Proficiency (Written & Spoken)", 93, "#1E88E5", "Mampu berkomunikasi dan menulis dalam bahasa Inggris secara profesional."),
    ("🔍", "Critical Thinking & Analytical Research", 78, "#43A047", "Menganalisis masalah, mencari data, dan menarik kesimpulan yang tepat."),
    ("🐍", "Python Programming", 83, "#F9A825", "Membuat program, otomasi, dan aplikasi web sederhana dengan Python & Streamlit."),
    ("📊", "Accounting & Data Analysis", 80, "#8E24AA", "Memahami dasar akuntansi dan mengolah data untuk pengambilan keputusan."),
]

def short(name):
    return name.split("(")[0].strip()

st.markdown(
    """
    <style>
    .skill-card { border-radius: 16px; padding: 18px 20px; margin-bottom: 8px;
        background: rgba(128,128,128,0.08); border-left: 6px solid var(--c); }
    .skill-card h4 { margin: 0 0 4px 0; }
    .skill-card p  { margin: 0; opacity: .75; font-size: 0.92rem; }
    .skill-level   { font-size: 2rem; font-weight: 700; color: var(--c); }
    .bar-bg   { background: rgba(128,128,128,0.2); border-radius: 10px; height: 12px; margin-top: 10px; }
    .bar-fill { height: 12px; border-radius: 10px; background: var(--c); }
    </style>
    """,
    unsafe_allow_html=True,
)

# Radar chart + ringkasan
labels = [f"{s[0]} {short(s[1])}" for s in SKILLS]
values = [s[2] for s in SKILLS]

fig = go.Figure(go.Scatterpolar(
    r=values + values[:1],
    theta=labels + labels[:1],
    fill="toself",
    line=dict(color="#E1306C", width=3),
    fillcolor="rgba(225,48,108,0.25)",
    hovertemplate="%{theta}: %{r}%<extra></extra>",
))
fig.update_layout(
    polar=dict(radialaxis=dict(range=[0, 100], ticksuffix="%")),
    showlegend=False,
    margin=dict(l=60, r=60, t=30, b=30),
    height=450,
    paper_bgcolor="rgba(0,0,0,0)",
)

left, right = st.columns([3, 2], vertical_alignment="center")

with left:
    st.plotly_chart(fig, use_container_width=True)

with right:
    top = max(SKILLS, key=lambda s: s[2])
    st.metric("Skill terkuat", f"{top[0]} {top[2]}%", short(top[1]))
    st.metric("Rata-rata semua skill", f"{round(sum(values) / len(values))}%")

st.divider()

# Kartu skill (2 kolom)
st.subheader("Detail Skill")
cols = st.columns(2, gap="large")

for i, (icon, name, level, color, desc) in enumerate(SKILLS):
    with cols[i % 2]:
        st.markdown(
            f'<div class="skill-card" style="--c:{color}">'
            f'<div class="skill-level">{level}%</div>'
            f"<h4>{icon} {name}</h4><p>{desc}</p>"
            f'<div class="bar-bg"><div class="bar-fill" style="width:{level}%"></div></div>'
            "</div>",
            unsafe_allow_html=True,
        )

st.divider()

_, kanan = st.columns([4, 1])
with kanan:
    st.page_link(
        "pages/Social Media.py", 
        label="Next", 
        icon="➡️")
