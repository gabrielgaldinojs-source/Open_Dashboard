import streamlit as st
 
from acesso_sheets import carregar_dados
 
import pandas as pd
 
st.set_page_config(page_title="Dashboard de KPIs", layout="wide")
 
st.title("📊 Painel de Controle de Entregas")
 
try:
     df = carregar_dados()
     st.success("Dados carregados em tempo real!")
 
     st.sidebar.header("Filtros")
 
     clientes = df['Cliente'].unique()
     
     filtro_cliente = st.sidebar.multiselect("Selecione o Cliente:", options=clientes, default=clientes)
 
     df_filtrado = df[df['Cliente'].isin(filtro_cliente)]
 
     col1, col2, col3 = st.columns(3)
 
     with col1:
         st.metric("Total de Pedidos", len(df_filtrado))
         
     with col2:
         total_caixas = df_filtrado['Qtde de caixas'].sum()
         st.metric("Total de Caixas", total_caixas)
         
     with col3:
         valor_total = df_filtrado['Valor da caixa'].sum()
         st.metric("Faturamento Total", f"R$ {valor_total:,.2f}")
 
     st.divider()
 
     st.subheader("Volume por Cliente")
     st.bar_chart(df_filtrado.set_index('Cliente')['Qtde de caixas'])
 
     st.subheader("Dados Detalhados")
     st.dataframe(df_filtrado, use_container_width=True)
 
except Exception as e:
     st.error(f"Erro ao carregar o dashboard: {e}")