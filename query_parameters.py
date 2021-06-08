from fastapi import FastAPI
from typing import Optional
import uvicorn 

app = FastAPI()

fake_items_db = [
        {"item_name": "foo"},{"item_name":"bar"}, {"item_name":"Barrilla"}
    ]
"""
# simple query parameters 
# herein they coverpassing int as the params int and limit
@app.get('/items/')
async def read_item(skip: int=0, limit:int=10):
    return fake_items_db[skip: skip+limit]
"""

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     """
#     async function that the takes item_id, q, short as params 
#     then assigns item_id str to the item dictionary, ??? why didn't he use
#     kw arguments, i guess with that q flag, he then he adds the q to the dict
#     else he assigns the adds a description entry to the dict.
#     """
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item


if __name__ == '__main__':
    uvicorn.run(app, port=8001, host='localhost')

