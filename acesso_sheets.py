import gspread
# Importa a biblioteca principal para interagir com o Google Sheets.

from google.oauth2.service_account import Credentials
# Importa o sistema de autenticação para usar o seu arquivo JSON.

import pandas as pd
# Importa o Pandas para transformar os dados da planilha em tabelas (DataFrames).

import os
# Importa funções do sistema operacional para lidar com caminhos de arquivos.

# Configuração de Acesso
# Define o que o seu código terá permissão de fazer no Google Drive e Sheets.
scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Autenticação
# Carrega as suas credenciais do arquivo JSON que você baixou do Google Cloud.
# Substitua pelo nome exato do seu arquivo que aparece na imagem: 'projetinho-489100-b0a856e8e3cd.json'
creds = Credentials.from_service_account_file(
    "projetinho-489100-b0a856e8e3cd.json",
    scopes=scopes
)

# Cria o cliente que será usado para abrir as planilhas.
client = gspread.authorize(creds)

def carregar_dados():
    # Abre a planilha pelo nome exato que você deu no Google Drive.
    planilha = client.open("Respostas_Forms")
    
    # Seleciona a primeira aba da planilha (onde o Forms joga as respostas).
    aba = planilha.sheet1
    
    # Pega todos os dados da aba e transforma em uma lista de dicionários.
    dados = aba.get_all_records()
    
    # Converte essa lista no formato de tabela do Pandas e retorna para o programa.
    return pd.DataFrame(dados)

# Teste simples para verificar se está funcionando
if __name__ == "__main__":
    try:
        df = carregar_dados()
        # Chama a função para buscar os dados.
        
        print("✅ Dados carregados com sucesso!")
        print("-" * 30)
        print(df.head()) 
        # Exibe as primeiras 5 respostas do formulário.
        print("-" * 30)
        
    except gspread.exceptions.SpreadsheetNotFound:
        print("❌ Erro: A planilha 'Respostas_Forms' não foi encontrada. Verifique o nome!")
    except gspread.exceptions.APIError as e:
        print(f"❌ Erro de Permissão: Verifique se compartilhou a planilha com o e-mail do JSON. {e}")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")