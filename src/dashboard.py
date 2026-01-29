import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURAÇÃO DA PÁGINA 
st.set_page_config(page_title="Dashboard de Auditoria - MPRJ", layout="wide", page_icon="🕵️‍♂️")

st.title("🕵️‍♂️ Painel de Inteligência de Dados - Auditoria")
st.markdown("Painel consolidado de evidências de inconsistências em contratos públicos.")
st.divider()

# CARREGAMENTO DOS DADOS 
@st.cache_data
def load_data():
    try:
        df_pagamentos = pd.read_csv("data/anomalias_pagamento_excedente.csv")
        df_contratos = pd.read_csv("data/anomalias_contrato_estourado.csv")
        df_datas = pd.read_csv("data/anomalias_datas_invalidas.csv")
        df_fornecedores = pd.read_csv("data/analise_top_fornecedores.csv")
        return df_pagamentos, df_contratos, df_datas, df_fornecedores
    except FileNotFoundError:
        return None, None, None, None

df_pagamentos, df_contratos, df_datas, df_fornecedores = load_data()

# VERIFICAÇÃO
if df_pagamentos is None:
    st.error("🚨 ERRO: Arquivos CSV não encontrados! Verifique se os 4 arquivos estão na mesma pasta.")
    st.stop()

# INDICADORES
col1, col2, col3, col4 = st.columns(4)

col1.metric("🔴 Pagamentos > Empenho", f"{len(df_pagamentos)} casos")
col2.metric("💸 Impacto Financeiro", f"R$ {df_pagamentos['diferenca'].sum():,.2f}")
col3.metric("🔴 Contratos Estourados", f"{len(df_contratos)} contratos")
col4.metric("🟠 Datas Inválidas", f"{len(df_datas)} ocorrências")

st.markdown("---")

# GRÁFICOS
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Top Fornecedores")
    fig_forn = px.bar(
        df_fornecedores.head(10), 
        x="total_dinheiro_empenhado", 
        y="nome_fornecedor", 
        orientation='h',
        title="Maior volume de verba empenhada"
    )
    fig_forn.update_layout(yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig_forn, use_container_width=True)

with col_right:
    st.subheader("⏳ Anomalia Temporal")
    fig_datas = px.scatter(
        df_datas, 
        x="data_pagamento", 
        y="dias_de_erro",
        size="valor",
        color="dias_de_erro",
        title="Pagamentos feitos antes do Empenho"
    )
    st.plotly_chart(fig_datas, use_container_width=True)

# TABELAS 
st.subheader("📋 Auditoria Detalhada")
tab1, tab2, tab3 = st.tabs(["💰 Pagamentos Excedentes", "📜 Contratos Estourados", "📅 Erros de Data"])

with tab1:
    st.dataframe(df_pagamentos.sort_values(by="diferenca", ascending=False), use_container_width=True)
with tab2:
    st.dataframe(df_contratos.sort_values(by="excesso", ascending=False), use_container_width=True)
with tab3:
    st.dataframe(df_datas.sort_values(by="dias_de_erro", ascending=False), use_container_width=True)