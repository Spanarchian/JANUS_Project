from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import logging
import time



from .janus_extract.reportcip import router as ciprouter
from .janus_ingest.message import router as messagerouter
from .janus_management.users import router as usersrouter
from .janus_management.auth import router as authrouter
 
api = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8100",
]
api.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
api.include_router(ciprouter)
api.include_router(messagerouter)
api.include_router(usersrouter)
api.include_router(authrouter)
 
@api.get("/")
def get_root():
    return {"status": {"Janus Core":"Operational"}}
 