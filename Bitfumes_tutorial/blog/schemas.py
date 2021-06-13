from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str

if __name__ == "__main__":
    pass
