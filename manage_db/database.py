# ⚠️ Dica de segurança:
# Depois que testar e confirmar que está funcionando, o ideal é guardar essa URL em uma variável de ambiente
#   (ex: os.getenv("DATABASE_URL")) para não deixar sua senha exposta no código.
# Mas no início, pode deixar direto no código enquanto estiver testando localmente.


# Aqui dou GET no DB, e depois importo ele onde precisar para mexer nele


# ------------------------------------------------------------------------
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_PUBLIC_URL = "postgresql://postgres:EDtvodUjGfrgsxCZGHGeIBLPfJStuSYz@crossover.proxy.rlwy.net:54736/railway"

# Cria a conexão com o banco de dados usando a URL pública fornecida pelo Railway
db = create_engine(DATABASE_PUBLIC_URL)

# Cria uma fábrica de sessões para interações com o banco (ex: consultas, inserções)
SessionLocal = sessionmaker(bind=db)

# Classe base usada para definir os modelos das tabelas (ORM)
Base = declarative_base()


