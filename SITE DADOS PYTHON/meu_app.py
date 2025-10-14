import streamlit as st 
import pandas as pd
st.set_page_config(page_title='Minha Página Streamlit')

with st.container():
    st.subheader('Meu site usando o Streamlit')
    st.title('Dashboard de Contratos')
    st.write('Informação dos contratos pela empresa Y no mes mês de maio')
    st.write('Site da B3 [Clique Aqui](https://www.b3.com.br/pt_br/para-voce)')

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv('resultados.csv')
    return tabela

with st.container():
    st.write("---")
    dados = pd.read_csv('resultados.csv')
    qtde_dias = st.selectbox('selecione o período', ["7 dias", "15 dias", "21 dias", "30 dias"])
    num_dias = int(qtde_dias.replace("dias",""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x='Data', y='Contratos')