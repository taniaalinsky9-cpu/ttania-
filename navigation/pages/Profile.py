import streamlit as st

st.set_page_config(page_title="Profile", page_icon="👩🏻", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FAF2D8;
    }
    .stApp p, .stApp li {
        font-size: 17px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    '<h2 style="display: inline; background-color: rgba(255, 182, 193, 0.6); padding: 2px 8px; border-radius: 25px;">Who Am I?</span></h2>', 
    unsafe_allow_html=True
)

st.divider()
coll1, coll2 = st.columns([3,2], gap="large")

with coll1 :
    st.title("Hello! Perkenalkan")
    st.write("aku Tania Alinsky. Aku lahir pada tanggal 30 Desember dan merupakan anak kedua dari tiga bersaudara. Sebagai anak tengah, aku belajar untuk bisa berbagi, beradaptasi, dan menjadi penengah di antara kakak dan adikku. Saat ini aku berkuliah di Universitas Nurdin Hamzah, mengambil program studi Sistem Informasi. Di jurusan ini aku mempelajari banyak hal, mulai dari akuntansi, pemrograman Python, sampai komunikasi")

with coll2 :
    st.image("image/profile.jpg", width=250)

st.markdown(
    "<p style='font-size:28px; font-weight:bold;'>t-tapi yang namanya manusia pasti punya hobbykan(?)</p>",
    unsafe_allow_html=True
)

coll3, coll4 = st.columns([1,2], gap="large")
with coll3 :
    st.image("image/tnbook.jpg", width = 250)

with coll4 :
    st.title("gues what? yup i love reading.")
    st.write("Ga niat gantiin Ariestoteles atau Socrates untuk jadi filsuf terkenal tapi setidaknya bisa jadi lawan ngobrol yang tau segalanya. ")

st.write("Kata orang-orang, setiap manusia harus punya motto hidup. Tapi kata Papa, “Motto hidup tuh nggak harus keren, Nak. Yang penting itu sesuai aja sama ambisi Adek.” Yeah... and proudly, I said:")

coll7, coll8 = st.columns(2)
with coll7 :
    st.title("ada seribu cara untuk menuju Roma, tapi ke China juga bagus")
with coll8 :
    st.image("image/cofused.jpg", width=300)

coll5, coll6 = st.columns([4, 1])

with coll6:
    st.page_link(
        "pages/Skill.py",
        label="Next",
        icon="➡️"
    )


