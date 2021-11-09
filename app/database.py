from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker
from .config import settings


SQLALCHEMY_database_url = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Using psycopg2
# while True:
#     try:
#         conn = psycopg2.connect(host = 'localhost', database = '', user='', password='', cursor_factory = RealDictCursor)
#         cursor = conn.cursor()
#         print('Database connection was successful')
#         break
#     except Exception as error:
#         print("Database connection failed")
#         print(error)
#         time.sleep(3)
