import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from manage_db.database import SessionLocal
from manage_db.models import Livro

st.title("Página - Tabela Livros 📚")

# ----------------------------------------------------------- Conecta ao banco e carrega dados

session = SessionLocal()
lista_livros = session.query(Livro).all()
session.close()

# Prepara os dados em formato de DataFrame
dados = [
    {
        "ID": livro.id,
        "Data": livro.data,
        "Título": livro.titulo,
        "Qtde Páginas": livro.qtde_paginas,
        "ID Usuário": livro.id_usuario,
    }
    for livro in lista_livros
]

df_livros = pd.DataFrame(dados)

# ----------------------------------------------------------- botões de ação

col1, col2 = st.columns(2)  # 💬 Divide a linha horizontalmente

# Adicionar
with col1:
    with st.container(border=True):
        # Botão para ir para a página de criação de novo livro
        st.page_link(
            label="➕ Adicionar novo livro",
            page="pages/2_pag_livros/2.1_pag_livros_create.py",
            icon="📗"
        )

# Editar
# Opção ao selctbox é mostrar o READ nao em df mas as linhas em 'objetos soltos'. Assim da pra acoplar um botao.
# Opção 2 é tentar com st.data_editor, se precisar, passar url da doc para gpt ler e ver se é possivel. Inclusive perguntar: se passar só a home da doc, vc lê tudo?
with col2:
    with st.container(border=True):
        # Dicionário {título: id} com opção em branco no topo
        opcoes = {"": None, **{livro.titulo: livro.id for livro in lista_livros}}

        # Dropdown de títulos (inicia em branco)
        livro_titulo_selecionado = st.selectbox(
            "Selecione um livro para editar:",
            options=list(opcoes.keys())
        )

        # Botão de editar, só funciona se um livro for selecionado
        if livro_titulo_selecionado and st.button("✏️ Editar Livro Selecionado"):
            st.session_state.id_livro_para_editar = opcoes[livro_titulo_selecionado]
            st.switch_page("pages/2_pag_livros/2.2_pag_livros_update.py")

# ----------------------------------------------------------- Separador visual
st.markdown("---")

# ----------------------------------------------------------- Exibição da tabela de livros
st.subheader("Lista de livros")
AgGrid(df_livros) # agrid fica aparecendo for trial use only. talvez melhor tentar com st.data_editor
