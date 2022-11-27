from fastapi import FastAPI
from router import get, post, calender
from fastapi.middleware.cors import CORSMiddleware
from db.models import Base
from db.database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(get.router)
app.include_router(post.router)
app.include_router(calender.router)

@app.get('/hello')
def index():
    return 'Hello World'