import streamlit as st
from router import router
from faq import faq_chain, ingest_faq_data
from pathlib import Path
from sql import sql_chain
from smart_talk import talk_to_ai
file_path=Path(__file__).parent / "resources" / "faq_data (1).csv"


st.title("E-commerce-chatbot")

query=st.chat_input("write you message")

ingest_faq_data(file_path)

def faq_sql(query):
    if query:
        route=router(query).name
        if route=="faq":
            return faq_chain(query)
        elif route=="talk":
            return talk_to_ai(query)
        else:
            return sql_chain(query) 
            



if "messages" not in st.session_state:
    st.session_state["messages"]=[]

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if query:
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role":"user","content":query})

    response=faq_sql(query)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role":"assistant","content":response})
