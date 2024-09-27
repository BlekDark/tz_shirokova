from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    apartment_number = Column(String, index=True)
    pet_name = Column(String)
    pet_breed = Column(String)
    walk_start = Column(DateTime)
    walk_end = Column(DateTime)


Base.metadata.create_all(bind=engine)
