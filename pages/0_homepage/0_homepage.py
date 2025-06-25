import streamlit as st

st.title("🏠 Pagina Inicial")
st.markdown("---")

with st.container(border=True):
    st.subheader("""
    Testes executados:
    - Autenticação (Login criptografado)
    - Permissões diferentes para usuários
    - Banco de dados:
        - Acesso seguro via variável de ambiente, tanto local quanto na nuvem.
        - CRUD 
            - Auto incremento
            - Chave estrangeira (Exclusão em cascata)
            - Senha criptografada
    """)
