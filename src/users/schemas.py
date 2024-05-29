from pydantic import BaseModel, Field, EmailStr

class OrmBaseModel(BaseModel):
    class Config:
        from_attributes = True

class UserBase(OrmBaseModel):
    email: str|None
    password:str
    is_active:bool = Field(default=False)

class UserRegister(BaseModel):
    email:EmailStr
    password:str


