import pandas as pd
import numpy as np
import streamlit as st
import time
import plotly.express as px
import matplotlib.pyplot as plt 

# Título e cabeçalhos
st.title('Explorando o Streamlit!')
st.header('Este é um cabeçalho')
st.subheader('Este é um subcabeçalho')
st.text('Este é um texto básico.')

# Formatação de texto
st.markdown('### Markdown é suportado!')
st.markdown('Podemos usar **negrito**, _itálico_, e até mesmo [links](http://streamlit.io)!')
st.markdown('---')

# Input de texto
st.header('Input de Texto')
input_text = st.text_input("Digite algo:")
if input_text:
    st.write("Você digitou:", input_text)
st.markdown('---')

# Text Area
st.header('Text Area')
input_area = st.text_area("Digite um texto mais longo aqui")
if input_area:
    st.write("Texto digitado:", input_area)
st.markdown('---')

# Caixa de Seleção
st.header('Seleção')
selected_option = st.selectbox("Selecione uma opção", ['Opção 1', 'Opção 2', 'Opção 3'])
if selected_option:
    st.write('Opção selecionada:', selected_option)
st.markdown('---')

# Multiselect
st.header('Multiselect')
selected_options = st.multiselect("Selecione uma ou mais opções", ['Opção A', 'Opção B', 'Opção C'])
if selected_options:
    st.write('Opções selecionadas:', selected_options)
st.markdown('---')

# Slider
st.header('Slider')
slider_value = st.slider("Escolha um valor", 0, 100, 50)
st.write("Valor escolhido:", slider_value)
st.markdown('---')

# Checkbox
st.header("Checkbox")
checkbox_state = st.checkbox("Marque para ativar")
st.write("Checkbox ativado:", checkbox_state)
st.markdown('---')

# Botão
st.header("Botão")
if st.button("Clique aqui"):
    st.write("Você clicou no botão!")
st.markdown('---')

# Radio Buttons
st.header("Radio Buttons")
radio_option = st.radio("Escolha uma opção", ['Opção 1', 'Opção 2', 'Opção 3'])
st.write("Você escolheu:", radio_option)
st.markdown('---')

# Progress bar
st.header("Barra de Progresso")
progress = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress.progress(i + 1)
st.markdown('---')

# Loading spinner
st.header("Loading")
with st.spinner("Aguarde..."):
    time.sleep(3)
st.success("Carregado com sucesso")
st.markdown('---')

# Upload de arquivos
st.header("Upload de Arquivos")
upload_file = st.file_uploader("Escolha um arquivo", type=['pdf', 'csv', 'txt'])
if upload_file:
    st.write("Nome do arquivo:", upload_file.name)
st.markdown('---')

# Exibindo dados em tabelas
st.header("Tabelas")
df = pd.DataFrame({
    'Coluna 1': [1, 2, 3, 4],
    'Coluna 2': [10, 20, 30, 40]
})
st.write("Tabela com `st.write`:")
st.write(df)

st.markdown('---')

st.write("Tabela com `st.dataframe`:")
st.dataframe(df)

st.markdown('---')

st.write("Tabela com `st.table`:")
st.table(df)
st.markdown('---')

# Gráficos
st.header("Gráficos")
data = {"x": [1, 2, 3, 4, 5], "y": np.log([10, 20, 30, 40, 50])}
st.line_chart(data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)
st.bar_chart(chart_data)
st.markdown('---')

# Mapas
st.header("Mapas")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)
st.markdown('---')

# Sidebar
st.sidebar.title("Barra Lateral")
st.sidebar.header("Demonstração da Barra Lateral")
sidebar_text = st.sidebar.text_input("Digite algo na barra lateral")
if sidebar_text:
    st.sidebar.write("Você digitou:", sidebar_text)

# Interatividade
#st.sidebar.markdown('---')
#sidebar_slider = st.sidebar.slider("Escolha um valor", 0, 100, 50)
#st.sidebar.write("Valor escolhido na barra lateral:", sidebar_slider)

# Exibindo Imagens
st.header("Imagens")
st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", caption="Streamlit Logo")
st.markdown('---')

# Exibindo Vídeos
st.header("Vídeos")
st.video("https://www.youtube.com/watch?v=B2iAodr0fOo")
st.markdown('---')


# Botão com callback
st.header('Botão com Callback')
if st.button('Clique aqui para ver uma mensagem'):
    st.write('Botão clicado! Esta mensagem aparece como resposta.')

# Formulário com callback
st.header('Formulário com Callback')
with st.form(key='my_form'):
    username = st.text_input('Usuário')
    password = st.text_input('Senha', type='password')
    submit_button = st.form_submit_button(label='Enviar')

if submit_button:
    st.write(f'Usuário: {username}, Senha: {password}')
st.markdown('---')

st.title('Layout Personalizado com Colunas')

col1, col2, col3 = st.columns(3)

with col1:
    st.header('Coluna 1')
    st.write('Conteúdo da coluna 1')

with col2:
    st.header('Coluna 2')
    st.write('Conteúdo da coluna 2')

with col3:
    st.header('Coluna 3')
    st.write('Conteúdo da coluna 3')
st.markdown('---')


st.title('Containers Expansíveis')

with st.expander("Clique para expandir"):
    st.write("Aqui está o conteúdo expansível!")
st.markdown('---')


st.title('Widgets Interativos')

# Date Input
st.header('Seleção de Data')
selected_date = st.date_input('Escolha uma data')
st.write('Data selecionada:', selected_date)

# Time Input
st.header('Seleção de Horário')
selected_time = st.time_input('Escolha um horário')
st.write('Horário selecionado:', selected_time)
st.markdown('---')

st.title('Integração com Plotly')

# Dados de exemplo
df = pd.DataFrame({
    'x': range(10),
    'y': [i**2 for i in range(10)]
})

# Gráfico interativo com Plotly
fig = px.line(df, x='x', y='y', title='Gráfico Interativo com Plotly')
st.plotly_chart(fig)
st.markdown('---')

st.title('Integração com Matplotlib')

# Dados de exemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Gráfico com Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(title='Gráfico com Matplotlib', xlabel='x', ylabel='sin(x)')

st.pyplot(fig)
st.markdown('---')