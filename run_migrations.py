import sqlalchemy as sql
import tomlkit as toml
from db.models import Base
import db.models

with open('.streamlit/secrets.toml', 'r') as secrets_file:
    config_data = toml.load(secrets_file)

sql_db_data = config_data['connections']['sql_db']

dialect  = sql_db_data['dialect']
username = sql_db_data['username']
password = sql_db_data['password']
host     = sql_db_data['host']
database = sql_db_data['database']

engine = sql.create_engine(f'{dialect}://{username}:{password}@{host}/{database}')

Base.metadata.create_all(engine)
