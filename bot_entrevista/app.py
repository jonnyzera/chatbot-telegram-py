# app.py
import streamlit as st
import pandas as pd

# Carrega a planilha
PLANILHA = "respostas.xlsx"

# Título do app
st.title("📋 Respostas dos Candidatos")

# Tenta carregar a planilha
try:
    df = pd.read_excel(PLANILHA)

    # Mostra a planilha
    st.subheader("📑 Dados Registrados")
    st.dataframe(df, use_container_width=True)

    # Filtro por candidato
    candidatos = df["Candidato"].unique()
    candidato_selecionado = st.selectbox("🔍 Filtrar por candidato:", ["Todos"] + list(candidatos))

    if candidato_selecionado != "Todos":
        df_filtrado = df[df["Candidato"] == candidato_selecionado]
        st.write(df_filtrado)
    else:
        st.write(df)

except FileNotFoundError:
    st.warning("❗ Arquivo 'respostas.xlsx' não encontrado.")
except Exception as e:
    st.error(f"Erro ao carregar a planilha: {e}")
