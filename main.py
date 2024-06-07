"""FastAPI Entrypoint"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.domain import DomainBase
from src.database import engine

from src.endpoints.default_endpoints import defaultEndpoints
from src.endpoints.student_endpoints import studentEndpoints

app = FastAPI()
#Database Scaffold (All at Once, No Migrations)
DomainBase.metadata.create_all(bind=engine)

#CORS -> https://aws.amazon.com/what-is/cross-origin-resource-sharing/
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

#Endpoints Registration
app.include_router(defaultEndpoints)
app.include_router(studentEndpoints)
