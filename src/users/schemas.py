from pydantic import BaseModel, Field

class OrmBaseModel(BaseModel):
    class Config:
        from_attributes = True

class UserBase(OrmBaseModel):
    email: str|None
    password:str
    is_active:bool = Field(default=False)

