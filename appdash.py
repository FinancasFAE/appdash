import streamlit as st
from yahooquery import Ticker
import pandas as pd
import plotly.graph_objects as go
# -*- coding: utf-8 -*-
# Lista de tickers
tickers = [
    "BRFS3.SA", "JBSS3.SA", "BEEF3.SA", "MRFG3.SA",
    "TSN", "HRL", "GIS"
]

st.set_page_config(page_title="Análise de Ações - Setor de Alimentos", layout="wide")
st.title("Dashboard Interativo - Ações do Setor de Alimentos")


# Seleção de ticker
selected_ticker = st.selectbox("Selecione uma ação:", tickers)

# Obtem dados do Yahoo
ticker_data = Ticker(selected_ticker)
hist = ticker_data.history(period="6mo", interval="1d").reset_index()

# Validação
if hist.empty:
    st.warning("Não foi possível obter os dados para esse ticker.")
else:
    # Gráfico de preços
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hist['date'], y=hist['close'], mode='lines', name='Preço de Fechamento'))
    fig.update_layout(title=f"Preço de Fechamento - {selected_ticker}", xaxis_title="Data", yaxis_title="Preço")
    st.plotly_chart(fig, use_container_width=True)

    # Estatísticas básicas
    st.subheader("Estatísticas")
    st.write(hist[['close', 'volume']].describe())

