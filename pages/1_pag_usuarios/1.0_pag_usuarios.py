import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

from manage_db.database import SessionLocal
from manage_db.models import Usuario

st.title('🧑️ Usuários')
st.markdown("---")


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
        "Senha": usuario.senha,
        "Ativo": usuario.ativo,
        "Admin": usuario.admin,
    }
    for usuario in lista_usuarios
]

# Cria o DataFrame
df_usuarios = pd.DataFrame(dados)

# ----------------------------------------------------------- botões de ação

col1, col2 = st.columns(2)  # 💬 Divide a linha horizontalmente

# Adicionar
with col1:
    with st.container(border=True):
        # Botão para ir para a página de criação de novo livro
        st.page_link(
            label="Adicionar novo usuário",
            page="pages/1_pag_usuarios/1.1_pag_usuarios_create.py",
            icon="➕"
        )

# Editar
# Opção ao selctbox é mostrar o READ nao em df mas as linhas em 'objetos soltos'. Assim da pra acoplar um botao.
# Opção 2 é tentar com st.data_editor, se precisar, passar url da doc para gpt ler e ver se é possivel. Inclusive perguntar: se passar só a home da doc, vc lê tudo?
with col2:
    pass
    with st.container(border=True):
        # Dicionário {título: id} com opção em branco no topo
        opcoes = {"": None, **{usuario.nome: usuario.id for usuario in lista_usuarios}}

        # Dropdown de títulos (inicia em branco)
        usuario_nome_selecionado = st.selectbox(
            "Selecione um usuario para editar:",
            options=list(opcoes.keys())
        )

        # Botão de editar, só funciona se um livro for selecionado
        if usuario_nome_selecionado and st.button("✏️️ Editar Usuário Selecionado"):
            st.session_state.id_usuario_para_editar = opcoes[usuario_nome_selecionado]
            st.switch_page("pages/1_pag_usuarios/1.2_pag_usuarios_update.py")

# --------------------------------------------------------------------------------------- Exibição df
# AgGrid(df_usuarios, height=400, width=150)
st.dataframe(df_usuarios, use_container_width=True, hide_index=True)
# ------------------------------------------------------------------------------------------ Permissões
with st.expander("Permissões"):
    with st.container(border=True):
        st.subheader('Não administrador')
        # Para treinar, OK! Mas permissão correta da pag Usuários seria:
        #     Admin - Vê todos os usuários: Inclui, Edita só o seu, Exclui.
        #     Não Admin - Vê apenas ao seu próprio usuário: Não Inclui, Edita, Não exclui.
        st.write("- No menu principal, não tem acesso à página 'Usuários'.")

        st.write("- Na página 'Editar Livros', não tem acesso à exclusão.")