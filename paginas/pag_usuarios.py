import streamlit as st
import pandas as pd  # necessário para montar o DataFrame
from manage_db.database import SessionLocal
from manage_db.models import Usuario

st.title('Página - Tabela Usuários')

# Cria uma nova sessão de banco de dados (boa prática: criar e fechar em cada uso)
session = SessionLocal()

# Consulta todos os usuários
lista_usuarios = session.query(Usuario).all()

# Fecha a sessão
session.close()

# Converte a lista de objetos ORM para uma lista de dicionários (para criar o DataFrame)
dados = [
    {
        "ID": usuario.id,
        "Nome": usuario.nome,
        "Email": usuario.email,
        "Ativo": usuario.ativo
    }
    for usuario in lista_usuarios
]

# Cria o DataFrame
df_usuarios = pd.DataFrame(dados)

# Exibe o DataFrame no Streamlit
st.dataframe(df_usuarios, use_container_width=True)
