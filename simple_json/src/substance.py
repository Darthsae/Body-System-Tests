from material import MaterialType

class Substance:
    def __init__(self, material: MaterialType, amount: float):
        self.material = material
        self.amount = amount