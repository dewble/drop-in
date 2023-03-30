from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello World, from Jeff"}


"""
CORS 예외 URL 등록
"""
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)