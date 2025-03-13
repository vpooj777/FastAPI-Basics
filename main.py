from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {'data': {'name': 'Rockstar', 'age': 25}}


@app.get('/about')
def about():
    return {'data': 'About Page'}
