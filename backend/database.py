from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
`SQLALCHEMY_DATABASE_URL`:접속 주소
`autocommit=False` : 데이터 변경 후 commit 사인을 주어야만 실제로 저장된다.
`create_engine` : 커넥션 풀 생성
"""
SQLALCHEMY_DATABASE_URL = "sqlite:///./drop-in.db"

engin = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engin)

Base = declarative_base()


def get_db():
    """
    - db 세션 객체를 리턴하는 제너레이터 get_db 함수
    - 제너레이터 함수에 @contextlib.contextmanager 어노테이션을 적용했으므로 다음과 같이 with 문과 함께 사용할 수 있다.
        - with get_db() as db:      # db 세 션 객 체 를 사 용 한 다 .
    - with 문을 벗어나는 순간 get_db 함수의 finally 작성한 db.close()함수가 자동으로 실행된다.
    :return: db
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()