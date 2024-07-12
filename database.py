from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение к базе данных
user = 'postgres' 
password = 'secret_password'  # Ваш пароль
host = 'localhost'  # 'localhost' если сервер PostgreSQL на той же машине
port = 5432  # Стандартный порт, может быть изменен
database_name = 'KTZISZ'  

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database_name}')

# Создание базового класса для моделей
Base = declarative_base()

# Модель "Документ"
class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String)

# Создание таблицы (если ещё не создана)
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)

# Функция для получения сессии
def get_session():
    return Session()