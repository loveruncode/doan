from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
PORT = '3306' 
DATABASE = 'bdss'

URL_DATABASE = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
try:
    engine = create_engine(URL_DATABASE)
    connection = engine.connect()
    print("ket nói database thanh cong")
    connection.close()
except Exception as e:
    print(f"Connection to the database failed: {e}")
