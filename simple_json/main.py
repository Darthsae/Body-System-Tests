import json
from abc import ABC, abstractmethod

def debugDict(a_dict: dict) -> str:
    to_return: str = "{\n"
    for key, value in a_dict.items():
        to_return += f"  \"{key}\": {value},\n"
    return to_return[:-2] + "\n}"

class Serializable(ABC):
    @abstractmethod
    def to_dict(self) -> dict | None:
        ...
    
    @classmethod
    @abstractmethod
    def from_dict(cls, a_dict: dict):
        ...

class BodyPartType(Serializable):
    def __init__(self):
        ...
    
    def to_dict(self) -> dict | None:
        ...
    
    @classmethod
    def from_dict(cls, a_dict: dict):
        ...

class BodyPartInstance:
    def __init__(self):
        ...

class EntityType(Serializable):
    def __init__(self):
        ...
    
    def to_dict(self) -> dict | None:
        ...
    
    @classmethod
    def from_dict(cls, a_dict: dict):
        ...

class EntityInstance:
    def __init__(self):
        ...

print("Init")