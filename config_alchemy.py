from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime


DB_URL = "sqlite:///predictions.db"
engine = create_engine(DB_URL, echo=False)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sepal_length = Column(Float, nullable=False)
    sepal_width = Column(Float, nullable=False)
    petal_length = Column(Float, nullable=False)
    petal_width = Column(Float, nullable=False)
    predicted_class = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# Cria as tabelas no banco (em produção utilizar Alembic)
Base.metadata.create_all(engine)