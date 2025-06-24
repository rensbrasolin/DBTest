import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from manage_db.database import SessionLocal
from manage_db.models import Livro

st.title("📚 Livros")
st.markdown("---")

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
            label="Adicionar novo livro",
            page="pages/2_pag_livros/2.1_pag_livros_create.py",
            icon="➕"
        )

# Editar
# Opção ao selctbox é mostrar as linhas do READ nao em df, mas em 'objetos soltos'. Assim da pra acoplar um botao.
# Opção 2 é tentar com st.data_editor, se precisar, passar url da doc para gpt ler e ver se é possivel.
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
            # Exibição condicional baseada na flag admin do usuário
            if st.session_state.usuario.admin:
                st.switch_page("pages/2_pag_livros/2.2_pag_livros_update_admin.py")
            else:
                st.switch_page("pages/2_pag_livros/2.2_pag_livros_update_naoadmin.py")

# ----------------------------------------------------------- Exibição da tabela de livros
AgGrid(df_livros) # agrid fica aparecendo for trial use only. talvez melhor tentar com st.data_editor

# # Exibição condicional baseada na flag admin do usuário
# if st.session_state.usuario.admin:
#     # # Aqui: mesmo conteúdo provisório para admins
#     # st.page_link("pages/0_homepage/0_homepage.py", label="🏠 Início")
#     # st.page_link("pages/1_pag_usuarios/1.0_pag_usuarios.py", label="🧑️ Usuários")
#     # st.page_link("pages/2_pag_livros/2.0_pag_livros.py", label="📚 Livros")
# else:
