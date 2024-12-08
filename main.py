import openai
import streamlit as st
import langchain_openai
from langchain_openai import ChatOpenAI

openai.api_key = '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'
# ChatOpenAI 객체 생성 시 API 키 전달
chat_model = ChatOpenAI(api_key=openai.api_key)

# Streamlit 앱 시작
st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        result = chat_model.invoke(subject + "에 대한 시를 써줘")
        st.write(result.content)
