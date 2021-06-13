from sqlalchemy import create_engine
from sqlalchemy.ext import declarative
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALECHEMY_DB_URL = 'sqlite:///.blog.db'

engine = create_engine(SQLALECHEMY_DB_URL,
                        connect_args={"check_same_thread":False})

session = sessionmaker(bind=engine,autocommit=False, autoflush=False)

Base = declarative_base

if __name__=="__main__":
    pass