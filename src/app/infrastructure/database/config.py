from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# url = URL.create(
#     drivername="postgresql",
#     username="user",
#     password="pass",
#     host="db",
#     port=5432,
#     database="mi_db",
# )

url = URL.create(
    drivername="postgresql",
    username="test_user",
    password="test_password",
    host="localhost",  # o "127.0.0.1" si estás en tu máquina local
    port=5432,
    database="test_db",
)
engine = create_engine(url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
