import cohere
import streamlit as st


        

co = cohere.Client(api_key="")

message = "Can you tell me about LLMs?"

response = co.chat(
  model="command-r-plus",
	chat_history=[
    {"role": "USER", "text": "Hey, my name is Michael!"},
    {"role": "CHATBOT", "text": "Hey Michael! How can I help you today?"},
  ],
  message="Can you tell me about nlp?"
)

print(response.text) 