from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE = os.getenv("POSTGRES_DATABASE")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
