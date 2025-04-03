class Reaction:
    def __init__(self) -> None:
        pass

    from .data import Data
    @classmethod
    def from_dict(cls, data: Data, aDict: dict[str]):
        return cls()
