from fastapi import FastAPI
from tsutaerufriendly import asgi

app = asgi.get_application()
