class Item:
    def __init__(self, id: int, name: str, price: float, measurement_unit: str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.measurement_unit = measurement_unit
    
    def __repr__(self) -> str:
        return f"<class 'Item'>"
    
    def __str__(self) -> str:
        return f"Item: {self.id} | {self.name} | {self.price} | {self.measurement_unit}"
    