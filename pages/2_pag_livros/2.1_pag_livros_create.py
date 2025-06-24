import streamlit as st
from manage_db.database import SessionLocal
from manage_db.models import Livro

st.title("➕📚 Adicionar Novo Livro")

# Cria sessão com banco de dados
session = SessionLocal()

with st.form("form_livro", clear_on_submit=True):
    # Campos do formulário
    titulo = st.text_input("Título do livro")
    qtde_paginas = st.number_input("Quantidade de páginas", min_value=1)

    # Botão de envio
    botao_cadastrar = st.form_submit_button("Cadastrar")

    if botao_cadastrar:
        novo_livro = Livro(
            titulo=titulo,
            qtde_paginas=qtde_paginas,
            id_usuario=st.session_state.usuario.id  # pega id do usuário logado
        )
        session.add(novo_livro)
        session.commit()
        st.success("✅ Livro cadastrado com sucesso!")

# Fecha a sessão
session.close()

# Botão para voltar à lista
st.page_link("pages/2_pag_livros/2.0_pag_livros.py", label="Voltar para consulta de livros", icon="⬅️")
