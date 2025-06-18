from sqlalchemy import Column, Integer, String, Boolean
from manage_db.database import Base


# -------------------------------------------------------------------------------Criar o modelo ORM da tabela usuarios
class Usuario(Base):
    __tablename__ = "usuarios"

    # autoincrement inicia com 1, ver como resolver qdo for importar um DB existente
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)  # index ajuda em buscas.
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # email único
    senha = Column(String, nullable=False)
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Usuario(id={self.id}, nome='{self.nome}', email='{self.email}', ativo={self.ativo})>"


# -------------------------------------------------------------------------------

