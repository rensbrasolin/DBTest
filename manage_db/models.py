from manage_db.database import Base
from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date

# -------------------------------------------------------------------------------------- Modelo ORM da tabela 'usuarios'
class Usuario(Base):
    __tablename__ = "usuarios"  # Nome exato da tabela no banco de dados

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)  # Chave primária com índice
    nome = Column(String, nullable=False)  # Nome do usuário, obrigatório
    email = Column(String, nullable=False, unique=True)  # Email único, obrigatório
    senha = Column(String, nullable=False)  # Senha do usuário, obrigatório
    ativo = Column(Boolean, default=True)  # Campo para ativar/desativar o usuário
    admin = Column(Boolean, default=False)


    # Relacionamento com os livros cadastrados pelo usuário. (usuario.livros/livro.usuarios)
    livros = relationship(
        "Livro",                # Nome da classe relacionada
        back_populates="usuario",  # Refere-se ao atributo 'usuario' na classe Livro
        cascade="all, delete-orphan"  # Ao deletar um usuário, apaga também seus livros
    )

    def __repr__(self): # Nem todos campos retornam aqui. depois perguntar pq, pro gpt
        return f"<Usuario(id={self.id}, nome='{self.nome}', email='{self.email}', senha='{self.senha}', ativo={self.ativo}, admin={self.admin})>"


# ---------------------------------------------------------------------------------------- Modelo ORM da tabela 'livros'
class Livro(Base):
    __tablename__ = "livros"  # Nome exato da tabela no banco de dados

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)  # Chave primária com índice
    data = Column(Date, default=date.today)
    titulo = Column(String, nullable=False)  # Título do livro, obrigatório
    qtde_paginas = Column(Integer, nullable=False)  # Quantidade de páginas, obrigatório
    id_usuario = Column( #*************************************************************************************** Enquanto nao criar login, preencher isso com existentes
        ForeignKey("usuarios.id"),  # Define como chave estrangeira que aponta para 'usuarios.id'
        nullable=False              # Obrigatório ter um usuário associado
    )


    # Relacionamento reverso com a tabela de usuários. (usuario.livros/livro.usuarios)
    usuario = relationship(
        "Usuario",              # Nome da classe relacionada
        back_populates="livros"  # Refere-se ao atributo 'livros' na classe Usuario
    )

    def __repr__(self):
        return f"<Livro(id={self.id}, titulo='{self.titulo}', qtde_paginas={self.qtde_paginas}, id_usuario={self.id_usuario})>"


# ------------------------------------------------------------------------------------ Comentários campos de uma tabela
# Campos com default=... ou autoincrement=True são autogerados.
#
# Campos de chave estrangeira precisam ser preenchidos por você, porque o sistema não tem como saber qual usuário logado deve ser usado.
#
# A lógica do usuário logado é responsabilidade da aplicação (Streamlit), não do banco nem do SQLAlchemy.