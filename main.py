#!/usr/bin/env python3
from models.base_model import BaseModel

base1 = BaseModel()

print(base1.__dict__)
print(type(base1.created_at))
# print(type(base1.updated_at))

dict_return = base1.to_dict()
print(type(base1.created_at))
isofmt = base1.created_at.isoformat()
print(type(base1.created_at))
isofmt2 = base1.updated_at.isoformat()
