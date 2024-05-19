#!/usr/bin/env python3
"""
Follow the flow of serialization and deserialization
"""
from models import storage
from models.base_model import BaseModel

print("==== Instance Creation ====\n")
base = BaseModel()
print(base)
print("---- to_dict return ----")
for key in base.to_dict().keys():
    print("\t{}: ({}) - {}".format(key, type(base.to_dict()[key]), base.to_dict()[key]))

print("\n==== At Storage ====")
print(storage.all())
print("\n_____Storage, key, value_type and value_____")
for key in storage.all().keys():
    print("\t{}: ({}) - {}".format(key, type(storage.all()[key]), storage.all()[key]))

print("\n==== Saving the object ====")
base.save()

print("\n==== At Storage ====")
print(storage.all())
print("\n_____Storage, key, value_type and value_____")
for key in storage.all().keys():
    print("\t{}: ({}) - {}".format(key, type(storage.all()[key]), storage.all()[key]))

print("\n==== At Reload ====")
storage.reset()
storage.reload()

print("\n_____Storage, key, value_type and value_____")
for key in storage.all().keys():
    print("\t{}: ({}) - {}".format(key, type(storage.all()[key]), storage.all()[key]))

print("\n==== Reloaded Object ====")
base2 = BaseModel(**base.to_dict())
print(base2)
print("\n---- to_dict return ----")
for key in base.to_dict().keys():
    print("\t{}: ({}) - {}".format(key, type(base.to_dict()[key]), base.to_dict()[key]))
