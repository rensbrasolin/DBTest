import streamlit as st
from manage_db.database import SessionLocal
from manage_db.models import Usuario
from streamlit_authenticator.utilities.hasher import Hasher  # Criptografia da senha

st.title("✏️ Editar Usuário")

# ----------------------------------------------------------- Verifica se ID foi passado via session_state
if "id_usuario_para_editar" not in st.session_state:
    st.warning("Nenhum usuario selecionado para edição.")
    st.stop()

# ----------------------------------------------------------- Conecta ao banco e busca o livro
session = SessionLocal()
usuario_id = st.session_state.id_usuario_para_editar
usuario = session.query(Usuario).get(usuario_id)

if not usuario:
    st.error("Usuário não encontrado.")
    st.stop()

# ----------------------------------------------------------- Formulário com valores preenchidos

with st.form("form_editar_usuario"):
    nome = st.text_input("Nome", value=usuario.nome)
    email = st.text_input("Email", value=usuario.email)
    senha = st.text_input("Senha", type="password", value=usuario.senha)
    ativo = st.checkbox("Ativo?", value=usuario.ativo)
    admin = st.checkbox("Administrador?", value=usuario.admin)

    botao_salvar = st.form_submit_button("Salvar alterações")

    if botao_salvar:
        # Criptografia da senha
        senha_criptografada = Hasher.hash(senha)

        usuario.nome = nome
        usuario.email = email
        usuario.senha = senha_criptografada
        usuario.ativo = ativo
        usuario.admin = admin

        session.commit()
        st.success("✅ Usuário atualizado com sucesso!")

# ----------------------------------------------------------- Espaçamento visual
st.markdown("---")

# ----------------------------------------------------------- Confirmação antes de excluir
st.subheader("Excluir este usuário")

# 💬 Usa session_state interno para controlar a intenção de excluir
if "confirma_exclusao" not in st.session_state:
    st.session_state.confirma_exclusao = False

# Primeiro botão (mostrar intenção)
if not st.session_state.confirma_exclusao:
    if st.button("🗑️ Excluir Usuario"):
        st.session_state.confirma_exclusao = True
        st.warning("⚠️ Essa ação é irreversível. Marque a caixa abaixo para confirmar.")

# Exibe checkbox + botão de confirmação somente após clicar em excluir
if st.session_state.confirma_exclusao:
    confirma = st.checkbox("Sim, desejo excluir este usuário")

    if confirma:
        if st.button("❌ Confirmar Exclusão", type="primary"):
            session.delete(usuario)
            session.commit()

            # 💬 Limpa a flag de confirmação
            st.session_state.confirma_exclusao = False

            # 💬 Limpa o ID do livro
            st.session_state.pop("id_usuario_para_editar", None)

            st.success("Usuário excluído com sucesso! Redirecionando...")

            # Redireciona automaticamente após exclusão
            st.switch_page("pages/1_pag_usuarios/1.0_pag_usuarios.py")

# ----------------------------------------------------------- Fecha conexão com banco
session.close()

# ----------------------------------------------------------- Botão de voltar
st.page_link("pages/1_pag_usuarios/1.0_pag_usuarios.py", label="⬅️ Voltar para consulta de usuários", icon="🙋‍♂")
