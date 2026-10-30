import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F7F3E8;
    }
    .stApp p, .stApp li {
        font-size: 17px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

coll1,coll2 = st.columns (2)
with coll1 :
    st.title("WHO'S FORTOFOLIO (‘•.•’)?")

with coll2 :
    st.image("image/question.jpg", width=300)


col1, col2, col3 = st.columns (3)
with col1 :
    st.image("image/profile.jpg", width=180)
    st.page_link (
        "pages/Profile.py",
        label = "lihat profile"
    )
with col2 :
    st.image("image/tnbook.jpg", width=190)
    st.page_link (
        "pages/Skill.py",
        label = "lihat Skill"
    )
with col3 :
    st.image("image/cofused.jpg", width=230)
    st.page_link (
        "pages/Social Media.py",
        label = "lihat Social Media"
    )
