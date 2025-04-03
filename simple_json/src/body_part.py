from typing import Self

class BodyPartType:
    def __init__(self, bodyPartType: str, tags: dict[str], size: float):
        self.type = bodyPartType
        self.tags = tags
        self.size = size
    
    def __repr__(self) -> str:
        return f"{self.__dict__}"

    from .data import Data
    @classmethod
    def from_dict(cls, data: Data, bodyPartType: str, aDict: dict[str]) -> Self:
        """A
        """
        tags: dict[str] = aDict["tags"]
        size: float = aDict["size"]

        return cls(bodyPartType, tags, size)

class BodyPartInstance:
    from .data import Data
    def __init__(self, data: Data, bodyPartType: str, bodyPartID: str, bodyParts: list[dict[str]], tags: dict[str], size: float, reactions: list[dict[str]], parent: Self | None):
        """A
        """
        self.parent = parent
        self.type = bodyPartType
        self.id = bodyPartID
        self.tags = tags
        self.size = size
        from .reaction import Reaction
        self.reactions: list[Reaction] = [Reaction.from_dict(data, definition) for definition in reactions]
        self.bodyParts: list[BodyPartInstance] = [BodyPartInstance.from_dict(data, definition, self) for definition in bodyParts]
        from .substance import Substance
        self.substances: list[Substance] = []
    
    def update(self, entity: "EntityInstance", data: Data) -> None:
        for reaction in reactions:
            reaction.update(entity, data)

    from .substance import Substance
    def hasSubstance(self, id: str) -> bool:
        for substance in self.substances:
            if substance.material == id:
                return True
        return False

    def __repr__(self) -> str:
        return f"{self.__dict__}"
    
    @classmethod
    def from_dict(cls, data: Data, aDict: dict[str], parent: Self | None = None) -> Self | None:
        bodyPartType: BodyPartType = data.bodyPartTypes.get(aDict["type"], None)
        if bodyPartType == None:
            print(f"Error: BodyPartType of {aDict["type"]} does not exist.")
            return None
        overrides: dict[str] = aDict["overrides"]
        tags: dict[str] = bodyPartType.tags
        for tagName, value in overrides.get("tags", {}):
            if value is None:
                tags.pop(tagName, None) 
            else:
                tags[tagName] = value
        size: float = overrides.get("size", bodyPartType.size)
        return cls(data, bodyPartType.type, aDict["id"], aDict.get("body_parts", {}), tags, size, aDict.get("reactions", {}), parent)
