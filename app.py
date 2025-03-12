import streamlit as st
import pandas as pd
import requests

# Função para buscar licitações no ComprasNet
def buscar_licitacoes(palavra_chave=""):
    url = "https://compras.dados.gov.br/licitacoes/v1/licitacoes.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()["_embedded"]["licitacoes"]
        lista_licitacoes = []
        
        for item in dados:
            objeto = item.get("objeto", "Não informado")
            orgao = item.get("_links", {}).get("orgao", {}).get("title", "Não informado")
            valor = item.get("valor_estimado", "Não informado")

            if palavra_chave.lower() in objeto.lower():
                lista_licitacoes.append({"Órgão": orgao, "Objeto": objeto, "Valor Estimado": valor})
        
        return lista_licitacoes
    else:
        return []

# Interface Streamlit
st.title("Buscador de Licitações - Integração com ComprasNet")

# Campo de busca
busca = st.text_input("Digite uma palavra-chave para buscar licitações:", "")

# Buscar e exibir os dados
if busca:
    licitacoes = buscar_licitacoes(busca)
    if licitacoes:
        df = pd.DataFrame(licitacoes)
        st.dataframe(df)

        # Opção para baixar CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Baixar em CSV", csv, "licitacoes.csv", "text/csv")
    else:
        st.warning("Nenhuma licitação encontrada para essa palavra-chave.")