from dataclasses import dataclass


@dataclass(frozen=True)
class DatabaseConfiguration:
    dbname: str
    user: str
    password: str
    host: str
    port: str
    minconn: int
    maxconn: int
