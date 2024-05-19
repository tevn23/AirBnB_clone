#!/usr/bin/env python3
from models.base_model import BaseModel

base1 = BaseModel()
base1.name = "Our first model"
base1.number = 89

print("Initial Base attributes")
print(f"\t{base1.id}")
print(f"\t{base1}")

print("\nto_dict return:")
dict_return = base1.to_dict()
for key in dict_return:
    print(f"\t{key}: ({type(dict_return[key])}) - ({dict_return[key]})")

print("\nObject re-creation")
base2 = BaseModel(**dict_return)
print(f"\t{base2.id}")
print(f"\t{base2}")

print("\nAre they same object?")
print(base1 is base2)
