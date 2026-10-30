import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #E6E0F2;
    }
    .stApp p, .stApp li {
        font-size: 17px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    '<h2 style="display: inline; background-color: rgba(64, 164, 166, 0.4); padding: 2px 8px; border-radius: 25px;">Social Media</span></h2>', 
    unsafe_allow_html=True
)


st.set_page_config(page_title="Social Media", page_icon="📱", layout="wide")

SOCIALS = [
    ("📸", "Instagram", "https://www.instagram.com/caelumaether/", "#E1306C"),
    ("🎵", "TikTok", "https://www.tiktok.com/aetaether", "#00B3B3"),
]
TARGET = "_self"
st.markdown(
    """
    <style>
    .social-card { display: block; text-decoration: none !important; color: inherit !important;
        border-radius: 16px; padding: 18px 20px; margin-bottom: 14px;
        background: rgba(128,128,128,0.08); border-left: 6px solid var(--c);
        transition: transform .15s, background .15s; }
    .social-card:hover { transform: translateY(-3px); background: rgba(128,128,128,0.16); }
    .social-card h4 { margin: 0 0 4px 0; color: var(--c); }
    .social-card p  { margin: 0; opacity: .75; font-size: 0.92rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.divider()

cols = st.columns(2, gap="large")
for i, (icon, name, url, color) in enumerate(SOCIALS):
    with cols[i % 2]:
        st.markdown(
            f'<div><a class="social-card" href="{url}" target="{TARGET}" style="--c:{color}">'
            f"<h4>{icon} {name}</h4><p>",
            unsafe_allow_html=True,
        )

st.divider()
coll5, coll6 = st.columns([4, 1])
with coll6:
    st.page_link(
        "Beranda.py",
        label="Next",
        icon="➡️"
    )