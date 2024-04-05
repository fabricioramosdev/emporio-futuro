from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.models import Base

# Replace the placeholders with your actual username, password, host, and database name
engine = create_engine("postgresql://udsi255l6s28mh:p1322b823585610f6af4a92c8fd930549dac33496380b4c239b9a8cd781761f98@c7gljno857ucsl.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/ddtsbc7fjh6kje")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

try:
    connection = engine.connect()
    print("Connection successful.")
    create_db_and_tables()
    connection.close()
except Exception as e:
    print(f"An error occurred: {e}")

