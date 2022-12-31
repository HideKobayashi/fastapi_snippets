from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return 'hello'

@app.get('/blog/category')
def category():
    return {"data": 'all category'}

@app.get('/blog/{id}')
def get_blog(id: int):
    return {"data": id}

@app.get('/blog')
def search_blog(limit: int = 10, published: bool = True):
    if published:
        return {"data": f"{limit}件" }
    else:
        return {"data": "非公開"}
