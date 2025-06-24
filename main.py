# import streamlit as st
# from typing import Optional
# from manage_db.database import SessionLocal
# from manage_db.models import Usuario
# from streamlit_authenticator.utilities.hasher import Hasher  # Para checar bcrypt hashes
#
# # ---------------------------------------------------------------------------- #
# # CONFIGURAÇÃO DA PÁGINA
# # ---------------------------------------------------------------------------- #
# # Usa toda a largura disponível para reduzir scroll horizontal em tabelas
# st.set_page_config(layout="wide")
#
# # ---------------------
# # https://pypi.org/project/streamlit-authenticator/#history
# # ---------------------
# # ---------------------------------------------------------------------------- #
# # FUNÇÃO: Verificação de credenciais
# # ---------------------------------------------------------------------------- #
# def verificar_credenciais(email: str, senha: str) -> Optional[Usuario]:
#     """
#     Valida email e senha contra o banco de dados.
#     Retorna o objeto Usuario se as credenciais estiverem corretas, ou None.
#     Captura ValueError caso o hash salvo esteja em formato inválido.
#     """
#     session = SessionLocal()
#     user = session.query(Usuario).filter_by(email=email).first()
#     session.close()
#
#     # Se não encontrar usuário, retorna None imediatamente
#     if not user:
#         return None
#
#     try:
#         # Compara a senha em texto com o hash armazenado no DB
#         if Hasher.check_pw(senha, user.senha):
#             return user
#         return None
#     except ValueError:
#         # Erro de formato inválido de hash (salt inválido)
#         st.error("Erro interno de autenticação: formato de senha inválido.")
#         return None
#
# # ---------------------------------------------------------------------------- #
# # ESTADO INICIAL DA SESSÃO
# # ---------------------------------------------------------------------------- #
# # Define flags de autenticação e armazena o usuário logado
# if "autenticado" not in st.session_state:
#     st.session_state.autenticado = False
#     st.session_state.usuario = None
#
# # ---------------------------------------------------------------------------- #
# # FLUXO DE LOGIN
# # ---------------------------------------------------------------------------- #
# if not st.session_state.autenticado:
#     # Layout mais agradável: usa colunas para posicionar o form na direita
#     col_esquerda, col_central, col_direita = st.columns([1, 1, 1])
#
#     with col_central:
#         # Título na tela de login
#         st.title("🔐 Fazer Login")
#         st.write("Bem-vindo ao sistema. Faça login para continuar.")  # Placeholder
#         with st.form("login_form", clear_on_submit=False):
#             # Campo de email
#             email = st.text_input("Email")
#             # Campo de senha
#             senha = st.text_input("Senha", type="password")
#             # Botão de envio
#             submitted = st.form_submit_button("Entrar")
#
#         # Se o usuário clicou em "Entrar"
#         if submitted:
#             # Verifica credenciais no DB
#             user = verificar_credenciais(email, senha)
#             if user:
#                 # Se OK, marca como autenticado e salva objeto user
#                 st.session_state.autenticado = True
#                 st.session_state.usuario = user
#                 st.success(f"✅ Bem-vindo(a), {user.nome}!")
#                 st.rerun()
#
#
#             else:
#                 # Senha ou email inválido
#                 st.error("❌ Usuário ou senha inválidos")
#     # Impede que o restante do app carregue antes do login
#     st.stop()
#
# # ---------------------------------------------------------------------------- #
# # AQUI: usuário já está autenticado
# # Você pode acessar st.session_state.usuario.nome, .email, .admin etc.
#
# # ---------------------------------------------------------------------------- #
# # MENU OCULTO (st.navigation) - registra todas as páginas, visíveis ou não
# # ---------------------------------------------------------------------------- #
# menu = st.navigation(
#     {
#         '🏠 Inicio': [
#             st.Page('pages/0_homepage/0_homepage.py', title='Início'),
#         ],
#         '🙋‍♂️ Usuários': [
#             st.Page('pages/1_pag_usuarios/1.0_pag_usuarios.py', title='Consultar Usuários'),
#             st.Page('pages/1_pag_usuarios/1.1_pag_usuarios_create.py', title='Adicionar Usuários'),
#             st.Page('pages/1_pag_usuarios/1.2_pag_usuarios_update.py', title='Editar Usuários'),
#         ],
#         '📖 Livros': [
#             st.Page('pages/2_pag_livros/2.0_pag_livros.py', title='Consultar Livros'),
#             st.Page('pages/2_pag_livros/2.1_pag_livros_create.py', title='Adicionar Livros'),
#             st.Page('pages/2_pag_livros/2.2_pag_livros_update.py', title='Editar Livros'),
#         ],
#     },
#     position="hidden"  # Oculta o menu lateral automático do Streamlit
# )
# menu.run()
#
# # ---------------------------------------------------------------------------- #
# # MENU VISÍVEL (Sidebar), condicionado ao tipo de usuário
# # ---------------------------------------------------------------------------- #
# with st.sidebar:
#     st.markdown("## 📚 Navegação")
#
#     # Se for admin, mostrar este bloco (por enquanto, mesmo conteúdo)
#     if st.session_state.usuario.admin:
#         # Links para usuários com perfil admin
#         st.page_link("pages/0_homepage/0_homepage.py", label="🏠 Início")
#         st.page_link("pages/1_pag_usuarios/1.0_pag_usuarios.py", label="🙋‍♂️ Usuários")
#         st.page_link("pages/2_pag_livros/2.0_pag_livros.py", label="📖 Livros")
#     else:
#         # Links para usuários não-admin (mesmos links por enquanto)
#         st.page_link("pages/0_homepage/0_homepage.py", label="🏠 Início")
#         st.page_link("pages/1_pag_usuarios/1.0_pag_usuarios.py", label="🙋‍♂️ Usuários")
#         st.page_link("pages/2_pag_livros/2.0_pag_livros.py", label="📖 Livros")
#
#     # Separador visual
#     st.markdown("---")
#
#     # Botão de logout sempre visível
#     if st.button("🔒 Logout"):
#         st.logout() # Se for usar só st.logout(), tentar declarar fx e por ele como uma página pra ver o que acontece.



# # ---------------------------------------------------------------------------------------------------------------------
# # Não se preocupar com frontend agora, fazer organizado mas básico. Depois ver com o cliente o que exigirá.
#
# Login resolvido. Não ficou do jeito que eu queria mas acho que dá pra começar assim.
# fazer deploy pra ver como o login funciona, inclusive em pcs diferentes e com mais de 1 usuario logado.


# parte 2
# mostrar qual usuario ta logado na pagina main de preferencia pois ai acho que da pra ficar e nao sumir independente de que pag usuario tiver
# criar arquivos diferentes para permissoes diferentes e por no menu tambem.


# corrigir tabela livros, jeito que pega id_usuario. agora ja pode pegar automatico



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # 2
import streamlit as st
from typing import Optional
from manage_db.database import SessionLocal
from manage_db.models import Usuario
from streamlit_authenticator.utilities.hasher import Hasher  # Utilitário para verificar hashes bcrypt

# ---------------------------------------------------------------------------- #
# CONFIGURAÇÃO DA PÁGINA
# ---------------------------------------------------------------------------- #
# Layout em tela cheia para evitar scroll horizontal em wide tables
st.set_page_config(layout="wide")

# ---------------------------------------------------------------------------- #
# FUNÇÃO: Verificação de credenciais
# ---------------------------------------------------------------------------- #
# Não consegui usar stauth pois authenticator.login() estava sempre None e nao consegui resolver
def verificar_credenciais(email: str, senha: str) -> Optional[Usuario]:
    """
    Consulta o usuário por email e compara o hash armazenado com a senha fornecida.
    Retorna o objeto Usuario se a autenticação for bem-sucedida, ou None caso contrário.
    Tratamento de erro ValueError para hashes em formato inválido.
    """
    # Abre sessão com o DB
    session = SessionLocal()
    user = session.query(Usuario).filter_by(email=email).first()
    session.close()

    # Se não encontrar usuário, retorna None imediatamente
    if not user:
        return None

    try:
        # Compara a senha em texto com o hash bcrypt no DB
        if Hasher.check_pw(senha, user.senha):
            return user
        # Senha incorreta
        return None
    except ValueError:
        # Hash no DB está corrompido ou em formato inválido
        st.error("Erro interno de autenticação: formato de senha inválido.")
        return None

# ---------------------------------------------------------------------------- #
# ESTADO INICIAL DO SESSION_STATE
# ---------------------------------------------------------------------------- #
# Garante as variáveis para controlar fluxo de autenticação
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
    st.session_state.usuario = None

# ---------------------------------------------------------------------------- #
# FLUXO DE LOGIN (manual)
# ---------------------------------------------------------------------------- #
if not st.session_state.autenticado:
    # Usa colunas para centralizar o form de login
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        # Cabeçalho e instruções
        st.title("🔐 Fazer Login")
        st.write("Bem-vindo ao sistema. Faça login para continuar.")

        # Formulário Streamlit temos text_input e submit
        with st.form("login_form", clear_on_submit=False):
            email = st.text_input("Email")  # campo de email
            senha = st.text_input("Senha", type="password")  # campo de senha
            submitted = st.form_submit_button("Entrar")  # botão de submit

        # Quando o usuário clica em Entrar
        if submitted:
            user = verificar_credenciais(email, senha)
            if user:
                # Autenticação bem-sucedida: atualiza session_state
                st.session_state.autenticado = True
                st.session_state.usuario = user
                st.success(f"✅ Bem-vindo(a), {user.nome}!")
                # Recarrega o app para renderizar o menu protegido
                st.rerun()
            else:
                # Feedback para credenciais inválidas
                st.error("❌ Usuário ou senha inválidos")
    # Interrompe a execução para não renderizar o restante antes do login
    st.stop()

# ---------------------------------------------------------------------------- #
# PONTO DE APÓS LOGIN BEM-SUCEDIDO
# ---------------------------------------------------------------------------- #
# Neste ponto, st.session_state.autenticado == True, e st.session_state.usuario está definido

# ---------------------------------------------------------------------------- #
# MENU OCULTO COM MULTIPAGE NAVIGATION
# ---------------------------------------------------------------------------- #
# Registrar todas as páginas (visíveis ou não) para a navegação interna
menu = st.navigation(
    {
        '🏠 Inicio': [st.Page('pages/0_homepage/0_homepage.py', title='Início')],
        '🙋‍♂️ Usuários': [
            st.Page('pages/1_pag_usuarios/1.0_pag_usuarios.py', title='Consultar Usuários'),
            st.Page('pages/1_pag_usuarios/1.1_pag_usuarios_create.py', title='Adicionar Usuários'),
            st.Page('pages/1_pag_usuarios/1.2_pag_usuarios_update.py', title='Editar Usuários'),
        ],
        '📖 Livros': [
            st.Page('pages/2_pag_livros/2.0_pag_livros.py', title='Consultar Livros'),
            st.Page('pages/2_pag_livros/2.1_pag_livros_create.py', title='Adicionar Livros'),
            st.Page('pages/2_pag_livros/2.2_pag_livros_update.py', title='Editar Livros'),
        ],
    },
    position="hidden"  # Oculta o menu lateral automático do Streamlit
)
menu.run()

# ---------------------------------------------------------------------------- #
# SIDEBAR: LINKS E LOGOUT, COM CONDIÇÃO DE ADMIN
# ---------------------------------------------------------------------------- #
with st.sidebar:
    st.markdown("## 📚 Navegação")

    # Exibição condicional baseada na flag admin do usuário
    if st.session_state.usuario.admin:
        # Aqui: mesmo conteúdo provisório para admins
        st.page_link("pages/0_homepage/0_homepage.py", label="🏠 Início")
        st.page_link("pages/1_pag_usuarios/1.0_pag_usuarios.py", label="🙋‍♂️ Usuários")
        st.page_link("pages/2_pag_livros/2.0_pag_livros.py", label="📖 Livros")
    else:
        # Mesmo conteúdo para usuários não-admin, ajuste depois conforme necessário
        st.page_link("pages/0_homepage/0_homepage.py", label="🏠 Início")
        st.page_link("pages/1_pag_usuarios/1.0_pag_usuarios.py", label="🙋‍♂️ Usuários")
        st.page_link("pages/2_pag_livros/2.0_pag_livros.py", label="📖 Livros")

    st.markdown("---")

    # Logout: botão simples que limpa sessão e redireciona para a homepage
    if st.button("🔒 Logout"):
        # Remove todas as chaves de session_state, garantindo que o usuário seja completamente deslogado
        st.session_state.clear()
        # Redireciona para a página inicial (homepage) para que o próximo login sempre comece lá
        # Usamos switch_page para evitar que o rerun preserve a rota anterior
        st.switch_page("pages/0_homepage/0_homepage.py")


        #     # Dá pra fazer logout assim, mas ele vai pra uma pagina em branco.
        #     if st.button("🔒 Logout"):
        #         st.logout()

# ---------------------------------------------------------------------------- #
# FIM DO SCRIPT
# ---------------------------------------------------------------------------- #

# --
# Comentários finais:
# - Esta abordagem é segura para apps internos e protótipos.
# - Usa bcrypt (via Hasher.check_pw) para comparação de senha.
# - session_state evita expor credenciais ou manter estado no cliente.
# - Para produção, considere:
#    * Usar HTTPS/TLS, variáveis de ambiente para configs sensíveis,
#    * Implementar bloqueio por várias tentativas inválidas,
#    * Usar sistema de OAuth/OIDC para maior segurança e SSO.
