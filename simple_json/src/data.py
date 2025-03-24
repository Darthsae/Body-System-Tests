class Data:
    def __init__(self):
        from .body_part import BodyPartType
        from .entity import EntityType
        self.bodyPartTypes: dict[str, BodyPartType] = {}
        self.entityTypes: dict[str, EntityType] = {}