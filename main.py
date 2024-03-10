from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Welcome to our news application!'}

@app.get('/news')
def get_news():
    return {'message': 'News endpoint'}