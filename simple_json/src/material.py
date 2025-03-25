from typing import Self

class MaterialType:
    def __init__(self, name: str, tags: dict[str], density: float):
        self.name = name
        self.tags = tags
        self.density = density
    
    from .data import Data
    @classmethod
    def from_dict(cls: Self, data: Data, materialType: str, aDict: dict[str]):
        return cls(materialType, aDict["tags"], aDict["density"])