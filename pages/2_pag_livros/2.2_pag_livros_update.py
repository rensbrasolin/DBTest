import streamlit as st
from manage_db.database import SessionLocal
from manage_db.models import Livro

st.title("✏️ Editar Livro")

# ----------------------------------------------------------- Verifica se ID foi passado via session_state
if "id_livro_para_editar" not in st.session_state:
    st.warning("Nenhum livro selecionado para edição.")
    st.stop()

# ----------------------------------------------------------- Conecta ao banco e busca o livro
session = SessionLocal()
livro_id = st.session_state.id_livro_para_editar
livro = session.query(Livro).get(livro_id)

if not livro:
    st.error("Livro não encontrado.")
    st.stop()

# ----------------------------------------------------------- Formulário com valores preenchidos
with st.form("form_editar_livro"):
    titulo = st.text_input("Título do livro", value=livro.titulo)
    qtde_paginas = st.number_input("Quantidade de páginas", min_value=1, value=livro.qtde_paginas)
    id_usuario = st.number_input("ID do usuário", min_value=1, value=livro.id_usuario)

    botao_salvar = st.form_submit_button("Salvar alterações")

    if botao_salvar:
        livro.titulo = titulo
        livro.qtde_paginas = qtde_paginas
        livro.id_usuario = id_usuario

        session.commit()
        st.success("✅ Livro atualizado com sucesso!")

# ----------------------------------------------------------- Espaçamento visual
st.markdown("---")

# ----------------------------------------------------------- Confirmação antes de excluir
st.subheader("Excluir este livro")

# 💬 Usa session_state interno para controlar a intenção de excluir
if "confirma_exclusao" not in st.session_state:
    st.session_state.confirma_exclusao = False

# Primeiro botão (mostrar intenção)
if not st.session_state.confirma_exclusao:
    if st.button("🗑️ Excluir Livro"):
        st.session_state.confirma_exclusao = True
        st.warning("⚠️ Essa ação é irreversível. Marque a caixa abaixo para confirmar.")

# Exibe checkbox + botão de confirmação somente após clicar em excluir
if st.session_state.confirma_exclusao:
    confirma = st.checkbox("Sim, desejo excluir este livro")

    if confirma:
        if st.button("❌ Confirmar Exclusão", type="primary"):
            session.delete(livro)
            session.commit()

            # 💬 Limpa a flag de confirmação
            st.session_state.confirma_exclusao = False

            # 💬 Limpa o ID do livro
            st.session_state.pop("id_livro_para_editar", None)

            st.success("Livro excluído com sucesso! Redirecionando...")

            # Redireciona automaticamente após exclusão
            st.switch_page("pages/2_pag_livros/2.0_pag_livros.py")

# ----------------------------------------------------------- Fecha conexão com banco
session.close()

# ----------------------------------------------------------- Botão de voltar
st.page_link("pages/2_pag_livros/2.0_pag_livros.py", label="⬅️ Voltar para consulta de livros", icon="📚")
