import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import time


def load_data():
    dataframe = pd.read_csv("SINASC_RO_2019.csv")[['munResLat','PARTO','IDANOMAL','CODMUNRES','munResLon','IDADEMAE','SEXO','APGAR1','APGAR5','PESO','CONSULTAS','DTNASC','GESTACAO','GRAVIDEZ','ESCMAE','ESTCIVMAE','IDADEPAI','GRAVIDEZ']]
    dataframe['DTNASC'] = pd.to_datetime(dataframe['DTNASC'])
    dataframe.dropna(inplace=True)
    return dataframe


def analises():
    data = load_data()

    st.sidebar.header('Escolha algumas análises:')
    selected_option = st.sidebar.radio("Escolha uma opção", ['CODMUNRES x IDANOMAL',
                                                           "Distribuição dos Partos",
                                                           "IDADEMAE x CONSULTAS",
                                                           "SEXO x PESO",
                                                           "Distribuição Idade Mães"
                                                           ])
    
    if selected_option:
        if selected_option == "Distribuição Idade Mães":
            st.header('Distribuição da Idade das Mães')
            plt.figure(figsize=(10, 6))
            sns.histplot(data['IDADEMAE'].dropna(), kde=True, bins=30)
            plt.title('Distribuição da Idade das Mães')
            plt.xlabel('Idade da Mãe')
            plt.ylabel('Frequência')
            st.pyplot(plt)
            
            with st.spinner("Aguarde..."):
                time.sleep(1)

            st.markdown('---')


        elif selected_option == "SEXO x PESO":
            st.header('Peso ao Nascer por Sexo')
            plt.figure(figsize=(10, 6))
            sns.boxplot(x='SEXO', y='PESO', data=data.dropna(subset=['PESO', 'SEXO']))
            plt.title('Peso ao Nascer por Sexo')
            plt.xlabel('Sexo')
            plt.ylabel('Peso (gramas)')
            st.pyplot(plt)
            
            with st.spinner("Aguarde..."):
                time.sleep(1)

            st.markdown('---')

        elif selected_option == "IDADEMAE x CONSULTAS":
            st.header('Número de Consultas Pré-natal por Idade da Mãe')
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x='IDADEMAE', y='CONSULTAS', data=data.dropna(subset=['CONSULTAS', 'IDADEMAE']))
            plt.title('Número de Consultas Pré-natal por Idade da Mãe')
            plt.xlabel('Idade da Mãe')
            plt.ylabel('Número de Consultas Pré-natal')
            st.pyplot(plt)
            
            with st.spinner("Aguarde..."):
                time.sleep(1)
  
            st.markdown('---')


        elif selected_option =="Distribuição dos Partos":
            st.header('Distribuição do Tipo de Parto')
            plt.figure(figsize=(10, 6))
            sns.countplot(x='PARTO', data=data.dropna(subset=['PARTO']),hue='SEXO')
            plt.title('Distribuição do Tipo de Parto')
            plt.xlabel('Tipo de Parto')
            plt.ylabel('Frequência')
            st.pyplot(plt)
            st.markdown('---')
            with st.spinner("Aguarde..."):
                time.sleep(1)

           

        elif  selected_option == 'CODMUNRES x IDANOMAL':
            st.header('Anomalias Congênitas por Município')
            anomalias_por_municipio = data.dropna(subset=['CODMUNRES', 'IDANOMAL']).groupby('CODMUNRES')['IDANOMAL'].sum().reset_index()
            plt.figure(figsize=(15, 8))
            sns.barplot(x='CODMUNRES', y='IDANOMAL', data=anomalias_por_municipio)
            plt.title('Anomalias Congênitas por Município')
            plt.xlabel('Código do Município')
            plt.ylabel('Número de Anomalias')
            plt.xticks(rotation=90)
            st.pyplot(plt)
            
            with st.spinner("Aguarde..."):
                time.sleep(1)

            st.markdown('---')

def sidebar():
    st.set_page_config(page_title="SINASC Rondônia 2019",layout='wide')
    st.title("Exemplo de outra aplicação SINASC")
    st.markdown('---')
    st.sidebar.title("OPERACOES EXERCÍCIO")
    st.sidebar.image("data:image/png;base64,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")
    

def qualitative_temporal():
    df = load_data()
    df['Mes_Ano'] = df['DTNASC'].apply(lambda x: x.strftime("%Y-%m"))
    st.sidebar.header('Qualitativas pelo tempo')
    selected_option = st.sidebar.multiselect("Selecione:", ['SEXO', 'GESTACAO', 'ESCMAE'])

    if selected_option:
        for var in selected_option:
            plt.figure(figsize=(12, 6))
            sns.countplot(data=df, x='Mes_Ano', hue=var, palette='Spectral')
            plt.title(f'Distribuição de {var} ao longo do tempo')
            plt.xticks(rotation=90)
            st.write(f'Distribuição de {var} ao longo do tempo')
            with st.spinner("Aguarde..."):
                time.sleep(1)
            st.success("Carregado com sucesso")
            st.pyplot(fig=plt)
    pass


def mapa_mun():
    df = load_data()
    lat_lon_data = df[['munResLat','munResLon']]
    lat_lon_data.dropna(inplace=True)
    lat_lon_data.rename(columns={'munResLat':'LAT','munResLon':'LON'},inplace=True)
    st.header('Municípios de Rondônia')
    st.map(lat_lon_data)
    st.markdown('---')


sidebar()
mapa_mun()
qualitative_temporal()
analises()
