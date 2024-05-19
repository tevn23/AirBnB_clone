#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
"""
print("\n+++ Storage Test +++")
print("__objects before update")
print(storage.all())
print("updating")
my_model.e_mail = "Awesome@mail.com"
print("saving")
my_model.save()
print("__objects after update\n")
print(storage.all())
print("Resetting")
storage.reset()
print("Reloading")
storage.reload()
print("__objects after reload")
print(storage.all())"""
