import streamlit as st
import pandas as pd
import sqlite3

# ==================== Funções de Banco ======================

# Conectar ao banco SQLite
def conectar_sqlite():
    try:
        conn = sqlite3.connect("banco.db")
        return conn
    except Exception as e:
        st.error(f"❌ Erro na conexão com o banco: {e}")
        return None

# Carregar dados dos pacientes
def carregar_dados_pacientes():
    try:
        conn = conectar_sqlite()
        query = """
            SELECT ID_PACIENTE, NOME, EMAIL, DATA_NASCIMENTO, TELEFONE
            FROM PACIENTE
        """
        dados = pd.read_sql_query(query, conn)
        conn.close()
        return dados
    except Exception as e:
        st.error(f"❌ Erro ao carregar dados de pacientes: {e}")
        return pd.DataFrame()

# Carregar dados dos sintomas
def carregar_dados_sintoma():
    try:
        conn = conectar_sqlite()
        query = """
            SELECT DATA, ID_SINTOMA, SINTOMA_DESCRICAO, GRAVIDADE
            FROM SINTOMA
        """
        dados = pd.read_sql_query(query, conn)
        conn.close()
        return dados
    except Exception as e:
        st.error(f"❌ Erro ao carregar dados de sintomas: {e}")
        return pd.DataFrame()

# ==================== Interface Streamlit ===================

st.set_page_config(page_title="Dashboard Odontológico", layout="wide")
st.title("🦷 Dashboard de Predição - Pacientes Odontológicos")

# Carregar dados
data_pacientes = carregar_dados_pacientes()
data_sintomas = carregar_dados_sintoma()

# Processar colunas de sintomas
if not data_sintomas.empty:
    data_sintomas.columns = data_sintomas.columns.str.lower().str.strip()
else:
    st.warning("⚠️ Dados de sintomas não carregados.")

# Mostrar dados dos pacientes
st.subheader("📑 Dados dos Pacientes")
if not data_pacientes.empty:
    st.dataframe(data_pacientes)
else:
    st.warning("⚠️ Nenhum dado de paciente encontrado.")

# Seleção de sintomas
if not data_sintomas.empty and 'sintoma_descricao' in data_sintomas.columns:
    sintomas_unicos = data_sintomas['sintoma_descricao'].dropna().unique()
else:
    sintomas_unicos = []
    st.warning("⚠️ Sintomas não encontrados no banco de dados.")

# ======================= Formulário ==========================
st.header("📝 Inserir Dados para Predição")

data_consulta = st.text_input("Data da consulta")

sintoma = st.selectbox("Sintoma", options=sintomas_unicos)

gravidade = st.slider("Gravidade do Sintoma (1-3)", min_value=1, max_value=3, value=2)

# ======================= Cálculo de risco =====================
def classificar_risco(gravidade):
    if gravidade == 1:
        return "Baixo"
    elif gravidade == 2:
        return "Médio"
    else:
        return "Alto"

risco = classificar_risco(gravidade)

st.subheader(f"🔍 **Risco Calculado:** {risco}")

# ==================== Recomendações ===========================
recomendacoes = {
    "Dor de cabeça": "💊 Tomar analgésico leve e repousar.",
    "Febre alta": "🌡️ Consultar um médico e manter hidratação.",
    "Náuseas": "🥤 Evitar alimentos gordurosos e manter hidratação.",
    "Cansaço extremo": "🛌 Descansar e verificar exames médicos.",
    "Tontura": "🩺 Monitorar pressão arterial e procurar auxílio médico se necessário."
}

tratamento = recomendacoes.get(sintoma, "Nenhuma recomendação específica encontrada.")
st.info(f"💡 **Recomendação:** {tratamento}")

if risco == "Alto":
    st.error("🚨 ALTA PRIORIDADE: O paciente precisa de atenção urgente!")
