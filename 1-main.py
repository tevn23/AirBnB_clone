#!/usr/bin/python3
import time
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(f"{obj_id}:\n\t{obj}")

print("\n-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
time.sleep(2)
my_model.save()
print(f"\t{my_model}")
