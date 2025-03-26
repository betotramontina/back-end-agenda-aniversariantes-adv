from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# Importa os elementos definidos no modelo
from model.base import Base
from model.contato import Contato

db_path = "database/"
# Verifica se o diretorio especificado para o banco de dados não existe
if not os.path.exists(db_path):
   # Então cria o diretorio
   os.makedirs(db_path)

# Define a URL de conexão com o banco de dados (SQLite local)
db_url = 'sqlite:///%s/db.sqlite3' % db_path

# Cria a engine de conexão com o banco de dados
engine = create_engine(db_url, echo=False)

# Instancia um criador de seções para interagir com o banco de dados
Session = sessionmaker(bind=engine)

# Cria o banco, caso ele ainda não tenha sido criado 
if not database_exists(engine.url):
    create_database(engine.url) 

# Cria as tabelas no banco de dados com base no modelo, caso ainda não existam
Base.metadata.create_all(engine)
