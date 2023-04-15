from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.review import review_router
from domain.comment import comment_router

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


# router 객체를 생성하여 FastAPI 앱에 등록해야만 라우팅 기능이 동작한다.
# 라우터 파일에 반드시 필요한 것은 APIRouter 클래스로 생성한 router객체이다.
app.include_router(review_router.router)
app.include_router(comment_router.router)