from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .schemas import Blog
from .database import engine,session_local
from . import models

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create(blog: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def search(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def get(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog

