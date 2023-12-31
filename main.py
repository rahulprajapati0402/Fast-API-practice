from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel

app = FastAPI()




@app.get('/')
def index():
    return {'data': {
        'name': "Rahul Prajapati",
        'company': "Cilans System"
    }}

@app.get('/about')
def about():
    return {'data': 'about page'}

@app.get('/blog')
def blog(limit=10, published: bool=True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs'}
    return {'data': f'{limit} blogs'}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'blog created with title {blog.title}'}