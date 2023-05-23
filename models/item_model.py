from typing import Union
from pydantic import BaseModel

#creación de una clase
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool,None] = None