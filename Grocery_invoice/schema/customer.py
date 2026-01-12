class Customer:
    def __init__(self, fname: str, lname: str) -> None:
        self.fname = fname
        self.lname = lname
    
    def __repr__(self) -> str:
        return f"<class 'Customer'>"
    
    def __str__(self) -> str:
        return f"First Name: {self.fname} Last Name: {self.lname}"
    
