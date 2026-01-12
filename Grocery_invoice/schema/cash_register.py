from .customer import Customer
from .invoice_item import Invoice_item
from datetime import datetime
from .item import Item

class Cash_register:
    def __init__(self, customer: Customer) -> None:
        self.customer = customer
        self.items: dict[str, Invoice_item] = {}
        self._gt_date = datetime.now()
        self._invoice_total: float = 0

    def get_items(self) -> str:
        items_string: str = "Item       |       Price       |       Quantity       |       Unit       |       discount \n" 
        for key, value in self.items.items():
            items_string += f"{key} | {value.item.price} | {value.quantity} | {value.item.measurement_unit} | {value.discount}\n"
        return items_string

    def __repr__(self) -> str:
        return f"<class 'Cash_register'>"
    
    def __str__(self) -> str:
        return f"Cash Register details: Customer Name: {self.customer.fname} {self.customer.lname}\nTotal items: {len(self.items)}\n{self.get_items()}"
    
    def _incre_total(self, item: Invoice_item) -> None:
        self._invoice_total += item.get_sub_total()

    def _decre_total(self, item: Invoice_item) -> None:
        self._invoice_total -= item.get_sub_total()
        
    def add_item(self, item: Item, quantity: int = 1, discount: float = 0) -> None:
        if item.name not in self.items.keys():
            new_item = Invoice_item(item=item, discount=discount, quantity=quantity)
            self.items[item.name] = new_item
            self._incre_total(new_item)
            print(f"Customer {self.customer.fname} {self.customer.lname} added {item.name} to cart.")
        else:
            print(f"Item: {item.name} already in cart. Want to update order???")
    
    def remove_item(self, name):
        if name in self.items.keys():
            old_item = self.items[name]
            self._decre_total(old_item)
            del self.items[name]
            print(f"Item {name} deleted successfully!!!")
        else:
            print(f"Item {name} not in the cart yet.")
    
    def update_item(self, item: Item, quantity: int = 1, discount: float = 0) -> None:
        if item.name in self.items.keys():
            self.remove_item(item.name)
            self.add_item(item, quantity, discount)
        else:
            print(f"Item {item.name} not in the cart yet. Want to add in the cart?")

    def get_invoice_total(self) -> float:
        return self._invoice_total

    def display_invoice(self):
        print("+" * 100)
        print(f"Customer: {self.customer.fname} {self.customer.lname}, Total Items: {len(self.items)}")
        print(f"Date: {self._gt_date.strftime('%B %d, %Y')}")
        print("-" * 100)
        for key, value in self.items.items():
            print(f"Item =>  {key}: ${value.item.price}/{value.item.measurement_unit}, Qty: {value.quantity}, Discount: ${value.discount}, Sub Total: {value._sub_total}")
        print("-" * 100)
        print(f"Total Price: ${self._invoice_total}")
        print("+" * 100)


    
        


