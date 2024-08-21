from os import getenv

from dotenv import load_dotenv
from psycopg2.pool import SimpleConnectionPool

load_dotenv()


connection_pool = SimpleConnectionPool(
    1,
    10,
)
