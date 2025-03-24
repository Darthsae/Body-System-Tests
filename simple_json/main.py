import json, os
from src.entity import EntityType, EntityInstance
from src.body_part import BodyPartType
from src.data import Data
from src.util import debugDict

def loadBodyParts(path: str, data: Data):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(".json"):
                with open(entry.path) as file:
                    info: dict[str] = json.load(file)
                    for name, value in info.items():
                        data.bodyPartTypes[name] = BodyPartType.from_dict(data, name, value)
            elif entry.is_dir():
                loadBodyParts(entry.path, data)

def loadEntityTypes(path: str, data: Data):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(".json"):
                with open(entry.path) as file:
                    info: dict[str] = json.load(file)
                    for name, value in info.items():
                        data.entityTypes[name] = EntityType.from_dict(data, name, value)
            elif entry.is_dir():
                loadEntityTypes(entry.path, data)

data: Data = Data()

loadBodyParts("sources/body_parts", data)
loadEntityTypes("sources/entities", data)

entity = EntityInstance(data, "Entity", data.entityTypes["bear"])

print(debugDict(entity.__dict__))

print("Init")