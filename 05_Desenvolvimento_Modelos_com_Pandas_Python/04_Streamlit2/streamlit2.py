import pandas            as pd
import seaborn           as sns
import streamlit         as st
import matplotlib.pyplot as plt
from PIL                 import Image
from io                  import BytesIO

custom_params = {"axes.spines.right":False,"axes.spines.top":False}
sns.set_theme(style='ticks',rc=custom_params)

#@st.cache_data
def load_data(file_data):
    try:
        return pd.read_csv(file_data,sep=';')
    except:
        return pd.read_excel(file_data,sep=';')

def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

def main():
    st.set_page_config(page_title="Telemarketing Analisys",
                       page_icon='icon.png',
                       layout='wide',
                       initial_sidebar_state='expanded')
    st.write("# Telemarketing Analisys")
    st.markdown("---")

    image = Image.open("bank.jfif")
    st.sidebar.image(image)

    st.sidebar.write("## Suba o arquivo")
    data_file_1 = st.sidebar.file_uploader("Bank marketing data",type=['csv','xlsx'])
    st.write(data_file_1)

    if data_file_1 is not None:

        bank_raw = load_data(data_file_1)
        bank = bank_raw.copy()

        st.write("## Antes dos filtros") 
        st.dataframe(bank_raw.head())
        st.write(f"{bank_raw.shape[0]} Linhas e {bank_raw.shape[1]} colunas")

        with st.sidebar.form(key='filtros_form'):

            radio_option = st.radio("Escolha o tipo de visualização", ['Barra', 'Pizza'])

            # Idades
            max_age = bank['age'].max()
            min_age = bank['age'].min()
            idades = st.slider(label="Intervalo Idades",
                            min_value=min_age,
                            max_value=max_age,
                            value=(min_age, max_age),
                            step=1)
            
            st.write(f"Menor valor: {idades[0]} e o maior valor: {idades[1]}")

            # Profissões
            st.markdown("---")
            st.write("### Filtros Data Frame")
            job_list = bank['job'].unique().tolist()
            job_list.append("All")

            selected = st.multiselect("PROFISSÃO", job_list, 'All')
            
            # Estado civil
            marital_list = bank['marital'].unique().tolist()
            marital_list.append('All')

            selected2 = st.multiselect("ESTADO CIVIL", marital_list, 'All')

            # Default
            default_list = bank['default'].unique().tolist()
            default_list.append('All')

            selected3 = st.multiselect("DEFAULT", default_list, 'All')

            # Financiamento imobiliário
            housing_list = bank['housing'].unique().tolist()
            housing_list.append('All')

            selected4 = st.multiselect("FINANCIAMENTO IMOB", housing_list, 'All')

            # Empréstimo
            loan_list = bank['loan'].unique().tolist()
            loan_list.append("All")
            
            selected5 = st.multiselect("EMPRÉSTIMO", loan_list, "All")

            # Contato
            contact_list = bank['contact'].unique().tolist()
            contact_list.append("All")
            
            selected6 = st.multiselect("CONTATO", contact_list, "All")

            # Mês
            month_list = bank['month'].unique().tolist()
            month_list.append("All")
            
            selected7 = st.multiselect("MÊS", month_list, "All")

            # Dia da semana
            day_of_week_list = bank['day_of_week'].unique().tolist()
            day_of_week_list.append("All")
            
            selected8 = st.multiselect("DIA DA SEMANA", day_of_week_list, "All")
            
            # Botão para aplicar os filtros
            submit_button = st.form_submit_button(label='Aplicar Filtros')

        if submit_button:
            bank = bank[(bank['age'] >= idades[0]) & (bank['age'] <= idades[1])]

            if "All" not in selected:
                bank = bank[bank['job'].isin(selected)].reset_index(drop=True)

            if "All" not in selected2:
                bank = bank[bank['marital'].isin(selected2)].reset_index(drop=True)

            if "All" not in selected3:
                bank = bank[bank['default'].isin(selected3)].reset_index(drop=True)

            if "All" not in selected4:
                bank = bank[bank['housing'].isin(selected4)].reset_index(drop=True)

            if "All" not in selected5:
                bank = bank[bank['loan'].isin(selected5)].reset_index(drop=True)

            if "All" not in selected6:
                bank = bank[bank['contact'].isin(selected6)].reset_index(drop=True)

            if "All" not in selected7:
                bank = bank[bank['month'].isin(selected7)].reset_index(drop=True)

            if "All" not in selected8:
                bank = bank[bank['day_of_week'].isin(selected8)].reset_index(drop=True)
    
        
        #---------------------------------------------------------------------------------------
        st.write("## Depois dos filtros")
        st.dataframe(bank.head())
        st.write(f"{bank.shape[0]} Linhas e {bank.shape[1]} colunas")        
        st.markdown("---")
        #---------------------------------------------------------------------------------------
        col1, col2 = st.columns(2)
        with col1:
            st.header('Proporção Original')
            bank_raw_target_perc = round((bank_raw[['age','y']].groupby('y').count().rename(columns={'age':'Percentual'})/bank_raw.shape[0])*100,2)
            st.write(bank_raw_target_perc)
            
            csv_raw = convert_df(bank_raw_target_perc)
            st.download_button(
                label="Download Proporção Original",
                data=csv_raw,
                file_name='proporcao_original.csv',
                mime='text/csv',
            )

        with col2:
            st.header('Proporção com filtros')
            bank_target_perc = round((bank[['age','y']].groupby('y').count().rename(columns={'age':'Percentual'})/bank.shape[0])*100,2)
            st.write(bank_target_perc)
            
            csv_filtered = convert_df(bank_target_perc)
            st.download_button(
                label="Download Proporção Filtrada",
                data=csv_filtered,
                file_name='proporcao_filtrada.csv',
                mime='text/csv',
            )
                
        #---------------------------------------------------------------------------------------

        st.write("## Visualização")

        #PLOTS
        if radio_option == 'Barra': 
            fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(8,5))

            sns.barplot(data=bank_raw_target_perc,
                        x=bank_raw_target_perc.index,
                        y='Percentual',ax=ax[0],
                        hue=bank_raw_target_perc.index,
                        palette='Blues')
            
            ax[0].bar_label(ax[0].containers[0])
            ax[0].set_title("Dados brutos",fontweight='bold')

            sns.barplot(data=bank_target_perc,
                    x=bank_target_perc.index,
                    y='Percentual',
                    ax=ax[1],
                    hue=bank_target_perc.index,
                    palette='Blues'
                )
            
            ax[1].bar_label(ax[1].containers[0])
            ax[1].set_title("Dados filtrados",fontweight='bold')

            st.pyplot(plt)
        else:
            colors = ['#1f77b4', '#ff7f0e']
            fig,ax = plt.subplots(nrows=1,ncols=2,figsize=(8,5))
            ax[0].pie(bank_raw_target_perc['Percentual'],labels=bank_target_perc.index,autopct='%1.1f%%',colors=colors,startangle=90)
            ax[0].set_title("Dados brutos",fontweight='bold')

            ax[1].pie(bank_raw_target_perc['Percentual'],labels=bank_target_perc.index,autopct='%1.1f%%',colors=colors,startangle=90)
            ax[1].set_title("Dados filtrados",fontweight='bold')

            st.pyplot(plt)

        # Botão de download para o dataframe filtrado
        st.markdown("---")
        st.write("### Download DataFrame Filtrado")
        csv_filtered_df = convert_df(bank)
        st.download_button(
            label="Download DataFrame Filtrado",
            data=csv_filtered_df,
            file_name='dataframe_filtrado.csv',
            mime='text/csv',
        )

main()






