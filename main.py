import streamlit as st


# Configurar o layout da página para ocupar toda a largura
st.set_page_config(layout="wide") # Fiz isso pra tabela não ficar pequena e com scroll horizontal.

# -------------------------------------------------------------------------------------------- Menu completo - oculto
# Define TODAS as páginas do app, inclusive as que devem ficar ocultas

menu = st.navigation(
    {
        '🏠 Inicio': [ # Posso pôr + desses títulos se necessário
            st.Page('pages/0_homepage/0_homepage.py', title='Início'),
        ],

        '🙋‍♂️ Usuários': [  # Posso pôr + desses títulos se necessário
            st.Page('pages/1_pag_usuarios/1.0_pag_usuarios.py', title='Consultar Usuários'),
        ],

        '📖 Livros': [  # Posso pôr + desses títulos se necessário
            st.Page('pages/2_pag_livros/2.0_pag_livros.py', title='Consultar Livros'),
            st.Page('pages/2_pag_livros/2.1_pag_livros_create.py', title='Adicionar Livros'),
            st.Page('pages/2_pag_livros/2.2_pag_livros_update.py', title='Editar Livros'),
        ],
    },
    position="hidden"  # 🔒 Oculta o menu lateral automático do Streamlit
)

menu.run()

# --------------------------------------------------------------------------------------------------------- Menu tela
with st.sidebar:  # ou em qualquer parte da tela
    st.markdown("## 📚 Navegação")

    # Links visíveis no menu manual
    st.page_link("pages/0_homepage/0_homepage.py", label="🏠 Início")
    st.page_link("pages/1_pag_usuarios/1.0_pag_usuarios.py", label="🙋‍♂️ Usuários")
    st.page_link("pages/2_pag_livros/2.0_pag_livros.py", label="📖 Livros")

    # ❌ Não inclui a página "Adicionar Livros" aqui para que fique oculta do menu
    # Mas ela ainda pode ser acessada por código com st.switch_page("2.1_pag_livros_create")


# ---------------------------------------------------------------------------------------------------------------------
# Não se preocupar com frontend agora, fazer organizado mas básico. Depois ver com o cliente o que exigirá

# Tentar o CRUD automatico por form. Daquele jeito separado.
#     Create - OK
#     Read - df aparece na tela, talvez por filtros depois, até pra usar no update.
#     Update - Tentar fazer ao lodo do create com dropdown
#     Delete: - Por botão na pagina que faz update

# Fazer deploy para testar CRUD pelo usuario na nuvem



# Se tudo isso funcionar, partir agora pro criar conta de acesso usuario







