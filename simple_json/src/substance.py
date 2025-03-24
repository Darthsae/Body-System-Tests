from material import Material

class Substance:
    def __init__(self, material: Material, amount: float):
        self.material = material
        self.amount = amount