# Enquanto aprendo como trabalhar melhor com DBs, vou deixar esse arquivo separado para rodar todas as ações no DB.
# Lógico que ele é o único que nao precisa ir pra nuvem.
# Deixar arquivo limpo de códigos. Códigos sensíveis deixar em arquivo txt

# Arquivos da pasta manage_db irão para a nuvem, não para serem rodados mas sim pq fazem a conexão con o DB


# Importando variáveis do DB. As outras importações fazer conforme necessidade de cada comando
from manage_db.database import db, SessionLocal, Base

# ---------------------------------------------------------------------------------------------------- Teste de conexão
if __name__ == "__main__":
    try:
        with db.connect() as conn:
            print("✅ Conexão com o banco realizada com sucesso!")
    except Exception as e:
        print("❌ Erro ao conectar no banco:", e)

# ----------------------------------------------------------------------------------------------------------------- Run

