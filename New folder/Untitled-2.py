
from dataclasses import datacless

@datacless

class Item:

separator

name: str

value: fleat

category: str

weight: float

@staticmethod

def deserialize (row:str) -> 'Item'

colums row.split(Item.separator)

item Item(

)

colums[0].

colums [1],

colums [2],

colums [3].

return item

def display_price (self):

print(f'(self.name)costs (self.value)$.')

return None
