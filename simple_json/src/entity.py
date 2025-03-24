from typing import Self
from .body_part import BodyPartType, BodyPartInstance

class EntityType:
    def __init__(self, entityType: str, bodyPlan: dict[str]):
        self.type = entityType
        self.bodyPlan = bodyPlan
    
    def __repr__(self) -> str:
        return f"{self.__dict__}"
    
    from .data import Data
    @classmethod
    def from_dict(cls: Self, data: Data, entityType: str, aDict: dict[str]):
        return cls(entityType, aDict["body_plan"])

class EntityInstance:
    from .data import Data
    def __init__(self, data: Data, name: str, entityType: EntityType):
        self.name = name
        self.type = entityType
        self.bodyPart = BodyPartInstance.from_dict(data, entityType.bodyPlan, None)