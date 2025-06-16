import streamlit as st


# Configurar o layout da página para ocupar toda a largura
st.set_page_config(layout="wide") # Fiz isso pra tabela não ficar pequena e com scroll horizontal.


menu = st.navigation(
    {
        '# Teste de Banco de Dados': [ # Posso pôr + desses títulos se necessário
            st.Page('paginas/pag_0.py', title='Início'),
            st.Page('paginas/usuarios.py', title='Usuários'),
            st.Page('paginas/livros.py', title='Livros')
        ],
    }
)

menu.run()