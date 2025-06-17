import streamlit as st
import pandas as pd
import plotly.express as px

# Dados
dados = {
    'Ano': [2022, 2023, 2024],
    'Atendimentos': [139567, 199879, 111086]  # 2024 até junho
}

df = pd.DataFrame(dados)

# Título
st.title("📈 Ansiedade em São Paulo (2022-2024)")

# Gráfico de barras
fig = px.bar(
    df,
    x='Ano',
    y='Atendimentos',
    text='Atendimentos',
    labels={'Atendimentos': 'Número de Atendimentos'},
    title='Evolução Anual de Atendimentos por Ansiedade'
)

fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

st.plotly_chart(fig)

# Observações em Markdown sem erro
st.markdown("""
### 📝 Observações:
- Os dados de **2024** correspondem apenas ao primeiro semestre.
- Houve um aumento de **43,21%** nos atendimentos de 2022 para 2023.
- Os dados foram obtidos da **Secretaria de Saúde de São Paulo**.
""")
