# Aqui dou GET no DB, e depois o importo onde precisar, para mexer nele.

# ------------------------------------------------------------------------------------------------ ⚠️ Dica de segurança
# Depois que testar e confirmar que está funcionando, o ideal é guardar essa URL em uma variável de ambiente
#   (ex: os.getenv("DATABASE_URL")) para não deixar sua senha exposta no código.
# Mas no início, pode deixar direto no código enquanto estiver testando localmente.

# ---------------------------------------------------------------------------------------------------------- HÍBRIDO
# Jeito 3: Resolve os 2 casos e não precisa ficar alterando codigo pra mexer no app local

"""
database.py
Módulo de conexão ao banco que funciona
tanto localmente (via .env) quanto na nuvem (Railway)
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv   # ← carrega o .env localmente

# ------------------------------------------------------------------
# 1) Carrega variáveis do .env SE o arquivo existir.
#    - Em produção não faz mal: se o arquivo não existir, não acontece nada.
# ------------------------------------------------------------------
load_dotenv()

# ------------------------------------------------------------------
# 2) Pega a URL do banco da variável de ambiente.
#    - No Railway: valor injetado automaticamente.
#    - Localmente: valor vindo do .env.
# ------------------------------------------------------------------
DATABASE_URL = os.getenv("DATABASE_URL")

# 3) Se mesmo assim for None, lançamos erro explícito
if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL não definida. "
        "Crie um arquivo .env com DATABASE_URL=... ou configure no Railway."
    )

# ------------------------------------------------------------------
# 4) Cria engine do SQLAlchemy
#    - pool_pre_ping evita sockets zumbis
#    - pool_size=5 é suficiente para até ~50 requisições simultâneas
# ------------------------------------------------------------------
db = create_engine(DATABASE_URL, pool_pre_ping=True, pool_size=5)

# Cria fábrica de sessão e classe Base
SessionLocal = sessionmaker(bind=db)
Base = declarative_base()


# # --------------------------------------------------------------------------------------------------------- LOCAL - 1
# # Jeito 1 acesso local: Direto pela URL do DB.
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
#
# DATABASE_PUBLIC_URL = ""
#
# # Cria a conexão com o banco de dados usando a URL pública fornecida pelo Railway
# db = create_engine(DATABASE_PUBLIC_URL)
#
# # Cria uma fábrica de sessões para interações com o banco (ex: consultas, inserções)
# SessionLocal = sessionmaker(bind=db)
#
# # Classe base usada para definir os modelos das tabelas (ORM)
# Base = declarative_base()


# --------------------------------------------------------------------------------------------------------- ONLINE - 2
# # 2 acesso online: pela varivavel de ambiente do Railway nuvem
#
# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
#

# # DATABASE_URL é variavel de ambiente criada la na parte de variáveis do app.
# # Na vdd ela puxa essa variavel que automaticamente já existe nas var de ambiente do objeto DB Railway.
# # Crio minha variavel DB_URL para diferenciar dos nomes padrão que existem.
# DB_URL = os.getenv("DATABASE_URL")
#
# # ➋ Cria engine e objetos ORM normalmente
# db = create_engine(DB_URL, pool_pre_ping=True, pool_size=5)
# SessionLocal = sessionmaker(bind=db)
# Base = declarative_base()









# --------------------------------------------------------------------------------------------------- INFORMAÇÕES ÚTEIS
# ) Referenciar a URL do banco no serviço do app (Criar var de ambiente)
# Abra o serviço do app (Teste DB → aba Variáveis).
#
# Clique em “+ NOVA variável”.
# Selecione o serviço Postgres e a variável DATABASE_URL (ou URL_DO_BANCO_DE_DADOS, depende do nome que o Railway gera).
# Dê um nome amigável, por exemplo DATABASE_URL.
# # ******************* Na vdd nao escolhi o nome, apenas escolhi (fix referencia) DATABASE_URL**************

# O painel criará algo como
# DATABASE_URL = {{ Postgres.DATABASE_URL }}
# (Railway faz a interpolação automática).

# 💡 Resumindo jeito seguro e eficiente de acessar o DB:
# Crie a variável DATABASE_URL no serviço do app apontando para o serviço do Postgres.
# Leia essa variável no Python com os.getenv("DATABASE_URL").
# Apague a string fixa do repositório.
# Para acessar localmente, crie arquvos .env (var de ambiente nele). E .gitignore e
    # faça como no código: procura local no .env. Ele só vai achar no .env se estivermos local pois o
    # .env não deve ir pra nuvem. Mesmo que vá, será 'bloquedo' pelo gitignore