
# 🦷 Dashboard de Predição - Pacientes Odontológicos

🚀 **[👉 Acesse o app online aqui](https://willyamdev-sprintia-main-2uloda.streamlit.app/)**  
🎥 **[👉 Assista à demonstração no YouTube](https://www.youtube.com/watch?v=KLoCCjDDZsI)**  
💻 **[👉 Acesse o código no GitHub](https://github.com/WillyamDev/SprintIA)**  

---

## 🎯 Sobre o Projeto 

A aplicação permite:  
- Visualizar dados de pacientes.  
- Consultar sintomas registrados.  
- Calcular o risco do paciente com base na gravidade dos sintomas.  
- Gerar recomendações automáticas.  
- Exibir alertas para casos de risco alto.  

O projeto utiliza banco de dados local **SQLite**, que não exige configuração de servidor ou autenticação.  

---

## 🗂️ Estrutura do Projeto

```
SprintIA3/
├── banco.db             # Banco de dados SQLite com os dados
├── main.py              # Código principal da aplicação Streamlit
├── requirements.txt     # Dependências do projeto
└── README.md            # Descrição do projeto
```

---

## ⚙️ Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- SQLite

---

## 🏗️ Estrutura do Banco de Dados

**Tabela PACIENTE:**  
- ID_PACIENTE (INTEGER PRIMARY KEY)  
- NOME (TEXT)  
- EMAIL (TEXT)  
- DATA_NASCIMENTO (TEXT)  
- TELEFONE (TEXT)  

**Tabela SINTOMA:**  
- ID_SINTOMA (INTEGER PRIMARY KEY)  
- DATA (TEXT)  
- SINTOMA_DESCRICAO (TEXT)  
- GRAVIDADE (INTEGER)  

---

## 🚀 Como Rodar Localmente

### 1️⃣ Clone o repositório:

```bash
git clone https://github.com/WillyamDev/SprintIA.git
cd SprintIA
```

### 2️⃣ Instale as dependências:

```bash
pip install -r requirements.txt
```

### 3️⃣ Execute o aplicativo:

```bash
streamlit run main.py
```

### 4️⃣ Acesse no navegador:

- Local: [http://localhost:8501](http://localhost:8501)  
- Ou em outro dispositivo na mesma rede: [http://seu-ip-local:8501](http://seu-ip-local:8501)


