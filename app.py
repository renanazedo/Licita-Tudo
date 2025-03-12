import streamlit as st
import pandas as pd

# Simulação de dados (substituir futuramente pela busca real no ComprasNet)
data = [
    {"ID": 1, "Órgão": "Ministério da Saúde", "Objeto": "Aquisição de Equipamentos Médicos", "Valor": "R$ 500.000,00"},
    {"ID": 2, "Órgão": "Prefeitura de São Paulo", "Objeto": "Serviço de Manutenção Predial", "Valor": "R$ 150.000,00"},
    {"ID": 3, "Órgão": "Governo do RJ", "Objeto": "Fornecimento de Alimentos", "Valor": "R$ 1.200.000,00"},
]

df = pd.DataFrame(data)

# Interface do Streamlit
st.title("Buscador de Licitações - Protótipo")

# Campo de busca
busca = st.text_input("Digite uma palavra-chave para buscar licitações:", "")

# Filtrando os resultados
if busca:
    df_filtrado = df[df["Objeto"].str.contains(busca, case=False, na=False)]
else:
    df_filtrado = df

# Exibir tabela
st.write("Resultados da Busca:")
st.dataframe(df_filtrado)

# Opção para download em CSV
csv = df_filtrado.to_csv(index=False).encode("utf-8")
st.download_button("Baixar em CSV", csv, "licitacoes.csv", "text/csv")

st.write("🚀 Esse é um protótipo inicial. No futuro, será conectado ao ComprasNet!")