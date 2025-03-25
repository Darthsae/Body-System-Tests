import json, os
from src.entity import EntityType, EntityInstance
from src.body_part import BodyPartType
from src.material import MaterialType
from src.data import Data
from src.util import debugDict

def loadBodyPartTypes(path: str, data: Data):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(".json"):
                with open(entry.path) as file:
                    info: dict[str] = json.load(file)
                    for name, value in info.items():
                        data.bodyPartTypes[name] = BodyPartType.from_dict(data, name, value)
            elif entry.is_dir():
                loadBodyPartTypes(entry.path, data)

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

def loadMaterialTypes(path: str, data: Data):
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(".json"):
                with open(entry.path) as file:
                    info: dict[str] = json.load(file)
                    for name, value in info.items():
                        data.materialTypes[name] = MaterialType.from_dict(data, name, value)
            elif entry.is_dir():
                loadMaterialTypes(entry.path, data)

data: Data = Data()

loadBodyPartTypes("sources/body_parts", data)
loadEntityTypes("sources/entities", data)
loadMaterialTypes("sources/materials", data)

entity = EntityInstance(data, "Entity", data.entityTypes["bear"])

print("Init")