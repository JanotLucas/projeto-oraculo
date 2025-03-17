import streamlit as st

st.title("Meu Chatbot Interativo")
st.write("Este é um exemplo simples de chatbot usando Streamlit no Google Colab.")

# Adicione seu modelo de chatbot aqui
user_input = st.text_input("Digite sua pergunta:")

if user_input:
    # Aqui você chamaria seu modelo para gerar uma resposta
    st.write(f"Resposta: {user_input} é uma pergunta interessante!")