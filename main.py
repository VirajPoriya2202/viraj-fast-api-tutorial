# install requirements.txt

from enum import Enum
from pydantic import BaseModel
from fastapi import FastAPI, Query

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


product_list = [{"name": "product 1"}, {"name": "product 2"}, {"name": "product 3"}, {"name": "product 4"}, ]


@app.get("/product")
async def product(skip: int = 0, limit: int = 10):
    return product_list[skip:skip + limit]


@app.get("/product/{product_id}", deprecated=False,
         description="This is example of the query parem which you need to pass in param")
async def get_product(product_id: str, q: str | None = None, short: bool = False):
    product = {
        "product_id": product_id,
    }
    if q:
        product.update({"q": q})
    if not short:
        product.update({"desc": "Hello short "})
    return product


class Item(BaseModel):
    name: str
    price: float
    description: str | None = None


@app.post("/add-item")
async def add_item(item: Item):
    return {"item": item}


@app.get("/add-query-validation")
async def add_query_validation(q: str | None = Query(None, min_length=3, max_length=10)):
    return {
        "q": q if q else "",
    }


@app.get("/add-query-validation/required-example")
async def add_query_validation(
        q: str = Query(..., min_length=3, max_length=10)):  # ... (this 3 dot means it is required)
    return {
        "q": q if q else "",
    }


# pass list in param with multiple str

@app.get("/add-query-validation/pass-multiple-str-in-param")
async def add_query_validation(
        q: list[int] = Query(..., min_length=1, max_length=10)):  # ... (this 3 dot means it is required)
    return {
        "q": q if q else "",
    }
