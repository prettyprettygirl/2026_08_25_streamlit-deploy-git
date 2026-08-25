from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

with st.sidebar:
    # openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

# 세션 스테이트에 대화 내용을 기록할 변수를 초기화 (최초 실행 시 한 번만 실행됨)
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# 세션 스테이트에 저장된 대화 내용을 화면에 출력 
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 사용자 입력을 대기 
if prompt := st.chat_input():
    # # API 키 입력 여부를 체크
    # if not openai_api_key:
    #     st.info("Please add your OpenAI API key to continue.")
    #     st.stop()

    # OpenAI 클라이언트 생성
    # client = OpenAI(api_key=openai_api_key)
    client = OpenAI()

    # 사용자 입력을 세션 스테이트에 기록하고 화면에 출력
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # 모델에 대화 내용을 전달하고 응답을 수신
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content

    # 모델의 응답을 세션 스테이트에 기록하고 화면에 출력
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
