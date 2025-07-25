from langchain_core.prompts import  ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
import os 
from dotenv import load_dotenv
load_dotenv()
#LANGCHAIN_API_KEY="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"
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_PROJECT']="Q&A chatbot with OLLAMA"

prompt = ChatPromptTemplate.from_messages([
    ("system","you are a helpful assitant. please provide response to the queries"),
    ("user","Question:{question}")
])
def generate_response(question,engine,temperature,max_tokens):
    
    llm=Ollama(model=engine)
    output_parser = StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({"question":question})
    return answer
st.title("Enhanced Q&A Chatbot with OLLAMA")



engine= st.sidebar.selectbox("select an OLLAMA Model", ["gemma2","mistral","phi3"])

temperature= st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value = 0.7)

max_tokens= st.sidebar.slider("Max_tokens",min_value=50,max_value=300,value=150)

st.write("Go Ahead and ask any question")
user_input= st.text_input("You:")

if user_input:
    response= generate_response(user_input,engine,temperature,max_tokens)
    st.write(response)
else:
    st.write("please provide the query")    
