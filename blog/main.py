from typing import List
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from passlib.context import CryptContext

from .database import engine, session_local
from . import models
from . import schemas
from .hashing import Hash


app = FastAPI()

models.Base.metadata.create_all(engine)

pwd_context = CryptContext(schemes=["bcrypt"])


origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog", status_code=status.HTTP_201_CREATED, tags=["blog"])
def create(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blog", response_model=List[schemas.ShowBlog], tags=["blog"])
def search(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blog/{id}", response_model=schemas.ShowBlog, tags=["blog"])
def get(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available.",
        )
    return blog


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blog"])
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not found.",
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return "Deletion complated."


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blog"])
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not found.",
        )
    blog.update(request.dict())
    db.commit()
    return "Update completed."


@app.post("/user", tags=["user"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    params = request.dict().copy()
    params.update({"password": Hash.bcrypt(request.password)})
    new_user = models.User(**params)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/user/{id}", response_model=schemas.ShowUser, tags=["user"])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} is not found.",
        )
    return user


@app.get("/user", response_model=List[schemas.ShowUser], tags=["user"])
def search_user(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
