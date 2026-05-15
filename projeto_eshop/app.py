import streamlit as st
from pymongo import MongoClient
import pandas as pd

# Conexão com o Banco da E-Shop Brasil
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
    db = client.eshop_db
    collection = db.clientes
    client.server_info() 
except:
    st.error("Aviso: O Banco de Dados (Docker) ainda não foi ligado!")

st.set_page_config(page_title="E-Shop Brasil - GTI", layout="wide")
st.title("🚀 E-Shop Brasil - Gestão de Big Data")

# Painel lateral para novos cadastros
st.sidebar.header("Painel do Gestor")
with st.sidebar.form("cadastro"):
    nome = st.text_input("Nome do Cliente")
    interesse = st.selectbox("Interesse Principal", ["Eletrônicos", "Moda", "Beleza", "Ferramentas"])
    botao = st.form_submit_button("Salvar no MongoDB")
    
    if botao and nome:
        collection.insert_one({"nome": nome, "categoria": interesse})
        st.sidebar.success(f"Dados de {nome} salvos com segurança!")

# Visualização da Base (Big Data em tempo real)
st.subheader("Análise de Preferências dos Clientes")
try:
    dados = list(collection.find({}, {"_id": 0}))
    if dados:
        st.table(pd.DataFrame(dados))
    else:
        st.info("Nenhum pedido registrado no sistema ainda.")
except:
    st.write("Conectando ao banco de dados...")