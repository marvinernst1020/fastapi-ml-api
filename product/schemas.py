from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    description: str
    price: int

class DisplaySeller(BaseModel):
    username: str
    email: str
    model_config = {
        "from_attributes": True
    }
    # class Config:
    #     orm_mode = True

class DisplayProduct(BaseModel):
    name: str
    description: str
    seller: DisplaySeller
    model_config = {
        "from_attributes": True
    }
    # class Config:
    #     orm_mode = True

class Seller(BaseModel):
    username: str
    email: str
    password: str

class Login(BaseModel):
    username: str
    password: str

class Toeken(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
