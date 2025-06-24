# Aqui dou GET no DB, e depois o importo onde precisar, para mexer nele.


# ------------------------------------------ ANTES DE FAZER DEPLOY, SEMPRE EXCLUIR, SE PERDER URL É SÓ PEGAR NO RAILWAY
# 1 acesso local: Direto pela URL do DB.


# --------------------------------------------------------------------- MAIS SEGURO. AO SUBIR, DEIXAR ESSE CÓD. VIGENTE
# 2 acesso online: pela varivavel de ambiente do Railway nuvem

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Crio minha variavel DB_URL para diferenciar dos nomes padrão qu existem.
# DATABASE_URL é variavel de ambiente criada la na parte de variáveis do projeto
DB_URL = os.getenv("DATABASE_URL")

# ➋ Cria engine e objetos ORM normalmente
db = create_engine(DB_URL, pool_pre_ping=True, pool_size=5)
SessionLocal = sessionmaker(bind=db)
Base = declarative_base()




# ------------------------------------------------------------------------------------------------ ⚠️ Dica de segurança
# Depois que testar e confirmar que está funcionando, o ideal é guardar essa URL em uma variável de ambiente
#   (ex: os.getenv("DATABASE_URL")) para não deixar sua senha exposta no código.
# Mas no início, pode deixar direto no código enquanto estiver testando localmente.

# --------------------------------------------------------------------------------------
# 2 ) Referenciar a URL do banco no serviço do app
# Abra o serviço do app (Teste DB → aba Variáveis).
#
# Clique em “+ NOVA variável”.
# Selecione o serviço Postgres e a variável DATABASE_URL (ou URL_DO_BANCO_DE_DADOS, depende do nome que o Railway gera).
# Dê um nome amigável, por exemplo DATABASE_URL.
# # ******************* Na vdd nao escolhi o nome, apenas escolhi (fix referencia) DATABASE_URL**************

# O painel criará algo como
# DATABASE_URL = {{ Postgres.DATABASE_URL }}
# (Railway faz a interpolação automática).

# 💡 Resumindo para leigos
# Crie a variável DATABASE_URL no serviço do app apontando para o serviço do Postgres.
# Leia essa variável no Python com os.getenv("DATABASE_URL").
# Apague a string fixa do repositório.