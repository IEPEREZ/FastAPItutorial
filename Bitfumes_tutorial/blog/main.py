from fastapi import FastAPI
from fastapi.param_functions import Body
import uvicorn
from pydantic import BaseModel
import schemas
app = FastAPI()


@app.post('/blog')


def create(request:schemas.Blog):
    return request

if __name__ == "__main__":
    uvicorn.run(app, port=8001, host='localhost')
