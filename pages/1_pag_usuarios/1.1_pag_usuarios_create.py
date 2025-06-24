import streamlit as st
from manage_db.database import SessionLocal
from manage_db.models import Usuario
from streamlit_authenticator.utilities.hasher import Hasher  # Criptografia da senha

st.title("📘 Adicionar Novo Usuário")
session = SessionLocal()

with st.form("form_usuario", clear_on_submit=True):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    ativo = st.checkbox("Ativo?", value=True)
    admin = st.checkbox("Administrador?", value=False)

    botao_cadastrar = st.form_submit_button("Cadastrar")
    if botao_cadastrar:
        # Criptografia da senha
        senha_criptografada = Hasher.hash(senha)

        novo_usuario = Usuario(
            nome=nome,
            email=email,
            senha=senha_criptografada,
            ativo=ativo,
            admin=admin,
        )
        session.add(novo_usuario)
        session.commit()
        st.success("✅ Usuário cadastrado com sucesso!")

session.close()
st.page_link("pages/1_pag_usuarios/1.0_pag_usuarios.py",
             label="⬅️ Voltar para consulta de usuários", icon="🙋‍♂️")
