from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from database import Base


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False)
    review_id = Column(Integer, ForeignKey("review.id"))        # 댓글을 리뷰와 연결하기 위해 추가한 속성. 댓글은 어떤 리뷰에 대한 댓글인지 알아야 하므로 id 속성이 필요하다.
    review = relationship("Review", backref="comments")        # 댓글 모델에서 리뷰 모델을 참조하기 위해 추가, comments.subject와 같이 사용할 수 있다.