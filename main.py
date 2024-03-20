# install requirements.txt
from uuid import UUID
from enum import Enum
from uuid import UUID
from datetime import datetime, time, timedelta
from pydantic import BaseModel, Field, HttpUrl, field_validator, EmailStr
from fastapi import FastAPI, Query, Path, Body, Header, Cookie

app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/user/")
# async def user_list():
#     return {"message": "All user list."}
#
#
# @app.get("/user/{id}")
# async def user_list(id: int):
#     return {"message": f"User id is {id}."}
#
#
# class ChoiceEnum(str, Enum):
#     one = "one"
#     two = "two"
#
#
# @app.get("/enum/{enum}")
# async def tutorial_enum(enum: ChoiceEnum):
#     if enum == ChoiceEnum.one:
#         return {"message": "You selected One."}
#     if enum == ChoiceEnum.two:
#         return {"message": "You selected Two."}
#
#
# product_list = [{"name": "product 1"}, {"name": "product 2"}, {"name": "product 3"}, {"name": "product 4"}, ]
#
#
# @app.get("/product")
# async def product(skip: int = 0, limit: int = 10):
#     return product_list[skip:skip + limit]
#
#
# @app.get("/product/{product_id}", deprecated=False,
#          description="This is example of the query parem which you need to pass in param")
# async def get_product(product_id: str, q: str | None = None, short: bool = False):
#     product = {
#         "product_id": product_id,
#     }
#     if q:
#         product.update({"q": q})
#     if not short:
#         product.update({"desc": "Hello short "})
#     return product
#
#
# class Item(BaseModel):
#     name: str
#     price: float
#     description: str | None = None
#
#
# @app.post("/add-item")
# async def add_item(item: Item):
#     return {"item": item}
#
#
# @app.get("/add-query-validation")
# async def add_query_validation(q: str | None = Query(None, min_length=3, max_length=10)):
#     return {
#         "q": q if q else "",
#     }
#
#
# @app.get("/add-query-validation/required-example")
# async def add_query_validation(
#         q: str = Query(..., min_length=3, max_length=10)):  # ... (this 3 dot means it is required)
#     return {
#         "q": q if q else "",
#     }
#
#
# # pass list in param with multiple str
#
# @app.get("/add-query-validation/pass-multiple-str-in-param")
# async def add_query_validation(
#         q: list[int] = Query(..., min_length=1, max_length=10)):  # ... (this 3 dot means it is required)
#     return {
#         "q": q if q else "",
#     }


# -----pass multiple body

# class Login(BaseModel):
#     username: str
#     password: str
#
#
# class User(BaseModel):
#     username: str
#     fullname: str
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None


# @app.put("/item/{item_id}")
# async def login(*,
#                 item_id: int = Path(..., title="The ID of the item to get"), ge=0, le=150,
#                 q: str | None = None,
#                 item: Item = Body(..., embed=True),
#                 # in case you only want get item and that need in dict like "item": {"name": "string","description": "string"}, in that case you can use embed=True
#                 user: User | None = None,
#                 importance: int = Body(...)
#                 # if you want get data in body and dont want create base class for that so you can do like importance: int = Body(...)
#                 ):
#     result = {"item_id": item_id}
#     if q:
#         result.update({"q": q})
#     if item:
#         result.update({"item": item})
#     if user:
#         result.update({"user": user})
#     if importance:
#         result.update({"importance": importance})
#     return result


# ------------------Body Fields --------------------------------
# class CreateItem(BaseModel):
#     name: str
#     description: str | None = Field(None, description="Please provide description in 300 char.", max_length=30)
#     price: float = Field(..., description="price must be greater then 0", gt=0)
#     tax: float | None = None
#
#
# @app.post("/create-item")
# async def create_item(*,
#                       # item: CreateItem,
#                       item: CreateItem = Body(..., embed=True),
#                       ):
#     result = {"item": item}
#     return result


# --------------------Body Nested models---------------------------------------------------------

# class Images(BaseModel):
#     url: HttpUrl
#     name: str
#
#
# class User(BaseModel):
#     user_id: int
#
#
# class CreateProduct(BaseModel):
#     name: str
#     desc: str | None = Field(..., description="add description", max_length=200)
#     tags: set[str] = []  # get multiple data list like ["hello","world"]
#     user: User  # if you want data in dict so you can do like this user:{"user_id":10}
#     images : list[Images]
#
#     @field_validator("tags")
#     def tags_must_have_at_least_one(cls, v):
#         if len(v) < 1:
#             raise ValueError("At least one tag is required")
#         return v
#
#     @field_validator("images")
#     def tags_must_have_at_least_one(cls, v):
#         if len(v) < 1:
#             raise ValueError("At least one tag is required")
#         return v
#
#
# @app.post("/create-product")
# async def create_product(
#         *,
#         product: CreateProduct
# ):
#     result = {"product": product}
#     return result


# --------------------Declare Request Example Data------------------------------------------------


# class Product(BaseModel):
#     name: str | None = None
#     description: str | None
#     price: float
#     tax: float

# name: str = Field(examples=["Foo"])
# description: str | None = Field(default=None, examples=["A very nice Item"])
# price: float = Field(examples=[35.4])
# tax: float | None = Field(default=None, examples=[3.2])

# model_config = {
#     "json_schema_extra": {
#         "examples": [
#             {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2,
#             }
#         ]
#     }
# }


# @app.post("/create-product")
# async def create_product(*, product: Product = Body(
#     openapi_examples={
#         "normal": {
#             "summary": "A normal example",
#             "description": "A **normal** item works correctly.",
#             "value": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2,
#             },
#         },
#         "converted": {
#             "summary": "An example with converted data",
#             "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
#             "value": {
#                 "name": "Bar",
#                 "price": "35.4",
#             },
#         },
#         "invalid": {
#             "summary": "Invalid data is rejected with an error",
#             "value": {
#                 "name": "Baz",
#                 "price": "thirty five point four",
#             },
#         },
#     },
# ),
#
#                          ):
#     result = {"product": product}
#     return result


# -----------------------------Extra Data Types--------------------------------------------------------------------------

# @app.put("/items/{item_id}")
# async def read_items(
#         item_id: UUID,
#         start_datetime: datetime | None = Body(default=None),
#         end_datetime: datetime | None = Body(default=None),
#         repeat_at: time | None = Body(default=None),
#         process_after: timedelta | None = Body(default=None),
#
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration,
#     }


# ------------------------------------Cookie Parameters and Header Parameters---------------------------------


# @app.get("/get-item")
# async def get_item(
#         cookie_id: str | None = Cookie(default=None),
#         x_token: list[str] | None = Header(default=None)
# ):
#     return {
#         "cookie_id": cookie_id,
#         "X-Token": x_token
#     }


# ------------------------------------Response Model - Return Type-----------------------------------------------------------

# class Item(BaseModel):
#     name: str
#     desc: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []
#
#
# @app.post("/create-item")
# async def create_item(item: Item):
#     return item


# example :--> 2
# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
#
#
# class UserIn(UserBase):
#     password: str
#
#
# class UserOut(UserBase):
#     pass
#
#
# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user

# example :--> 3

class Item(BaseModel):
    name: str
    desc: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
