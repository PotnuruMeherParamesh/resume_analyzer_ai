import streamlit as st
from analysis import analyzer_resume

st.set_page_config(page_title='CV Analyzer')

st.title('Resume Analyzer Using AI 🤖🧠🇦🇮')

st.subheader('''This page helps you to compare your resume with the given job description''')

st.sidebar.subheader('Drop your resume here ⬇️')
pdf_doc = st.sidebar.file_uploader('Click here to browse', type=['pdf'])

st.sidebar.markdown("Designed by Meher Paramesh")

st.sidebar.markdown("Github: 'https://github.com/PotnuruMeherParamesh'")

job_des = st.text_area('Copy and paste the JD here👉',max_chars=20000)

submit = st.button('Generate Score 📊')

if submit:
    with st.spinner('Getting results....'):
        analyzer_resume(pdf_doc,job_des)
    
