import gspread
 
from google.oauth2.service_account import Credentials
 
import pandas as pd
 
import streamlit as st
 
scopes = [
     "https://www.googleapis.com/auth/spreadsheets",
     "https://www.googleapis.com/auth/drive"
 ]
 
# Tente carregar das Secrets do Streamlit Cloud
creds_dict = dict(st.secrets["gcp_service_account"])
key = creds_dict.get("private_key", "")
if isinstance(key, str):
    key = key.strip().replace("\r\n", "\n").replace("\\n", "\n")
    creds_dict["private_key"] = key
creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
client = gspread.authorize(creds)

def carregar_dados():
    planilha = client.open("Respostas_Forms")
    aba = planilha.sheet1
    dados = aba.get_all_records()
    return pd.DataFrame(dados)
 
 
if __name__ == "__main__":
     try:
         df = carregar_dados()
         print("✅ Dados carregados com sucesso!")
         print("-" * 30)
         print(df.head()) 
         print("-" * 30)
         
     except gspread.exceptions.SpreadsheetNotFound:
         print("❌ Erro: A planilha 'Respostas_Forms' não foi encontrada. Verifique o nome!")
     except gspread.exceptions.APIError as e:
         print(f"❌ Erro de Permissão: Verifique se compartilhou a planilha com o e-mail do JSON. {e}")
     except Exception as e:
         print(f"❌ Ocorreu um erro inesperado: {e}")
