from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {"message":"Hello World"}

if __name__ == '__main__':
    uvicorn.run(app, port=8001, host='localhost')