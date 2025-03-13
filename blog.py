from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'message': "Hello Autobots!"}


@app.get('/about')
def about():
    return {'message': "This is Rockstar an Blog Site that is created by me"}


@app.get('/blog')
def blog():
    return {'Welcome to Rockstar Blog Site'}


@app.get('/blog')
@app.get('/blog/{id}')
def blog_id(id: int):
    return {'Blog ID': id}


@app.get('/blog/unpublished')
def unpublished():
    return {'message': " All Unpublished Blogs"}


@app.get('/blog/{id}/comments')
def blog_comments():
    return {'comments': 'Good Blogs'}


@app.get('/items/')
def read_items(name : str, price : float = 10.0):
    return {"name" : name, "price" : price}
