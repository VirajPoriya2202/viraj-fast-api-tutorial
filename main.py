# install requirements.txt

from enum import Enum

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user/")
async def user_list():
    return {"message": "All user list."}


@app.get("/user/{id}")
async def user_list(id: int):
    return {"message": f"User id is {id}."}


class ChoiceEnum(str, Enum):
    one = "one"
    two = "two"


@app.get("/enum/{enum}")
async def tutorial_enum(enum: ChoiceEnum):
    if enum == ChoiceEnum.one:
        return {"message": "You selected One."}
    if enum == ChoiceEnum.two:
        return {"message": "You selected Two."}
