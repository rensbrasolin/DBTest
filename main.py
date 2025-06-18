import streamlit as st


# Configurar o layout da página para ocupar toda a largura
st.set_page_config(layout="wide") # Fiz isso pra tabela não ficar pequena e com scroll horizontal.


menu = st.navigation(
    {
        '# Teste de Banco de Dados': [ # Posso pôr + desses títulos se necessário
            st.Page('paginas/pag_0.py', title='Início'),
            st.Page('paginas/pag_usuarios.py', title='Usuários'),
            st.Page('paginas/pag_livros.py', title='Livros')
        ],
    }
)

menu.run()



# ------------------------------------------
# Fazer deploy mandando pela 1a vez a pasta 'manage_db' para testar se a conexão com DB está funcionando na nuvem.

# Criar a outra tabela, livros.
# Tentar o CRUD automatico por form nas 2 páginas
# Fazer deploy para testar CRUD na nuvem

# Se tudo isso funcionar, partir agora pro criar conta de acesso usuario