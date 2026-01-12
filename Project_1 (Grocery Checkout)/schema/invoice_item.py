from .item import Item
class Invoice_item:
    def __init__(self, item: Item, discount: float, quantity: int) -> None:
        self.item = item
        self.discount = discount
        self.quantity = quantity
        self._sub_total = (item.price * quantity) - discount
    def __repr__(self) -> str:
        return f"<class 'Invoice_item'>"
    
    def __str__(self) -> str:
        return f"Invoice Item: {self.item} | {self.discount} | {self.quantity}"
    
    def get_sub_total(self) -> float:
        return (self._sub_total)
    
