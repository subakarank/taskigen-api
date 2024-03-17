from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
cors_origins = env_vars.get("CORS_ORIGINS", "").split()
app = FastAPI()

def add_cors_middleware(app: FastAPI):
  app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )

