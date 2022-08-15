from json import load

from pydantic import BaseModel, Field

from typing import Optional, List

class UserSchema(BaseModel):
    first_name: str = Field(max_length=12, min_length=4)
    last_name: str
    is_human: bool = Field(default=None)
    city: str
    arg: List[int]

with open("inpyt.json", "r", encoding="utf-8") as file:
    data = load(file)
