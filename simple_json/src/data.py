class Data:
    def __init__(self):
        from .body_part import BodyPartType
        from .entity import EntityType
        from .material import MaterialType
        self.bodyPartTypes: dict[str, BodyPartType] = {}
        self.entityTypes: dict[str, EntityType] = {}
        self.materialTypes: dict[str, MaterialType] = {}