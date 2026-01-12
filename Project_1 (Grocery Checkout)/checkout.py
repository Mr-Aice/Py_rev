import schema as p

def main()-> None:
    AWAIS = p.Customer(fname="Muhammad", lname="Awais")

    AHMED = p.Customer(fname="Ahmed", lname="Ali")

    i1 = p.Item(id=1,name="Eggs",price=40,measurement_unit="piece")
    i2 = p.Item(id=2,name="Green Tea",price=30,measurement_unit="Tag")
    i3 = p.Item(id=3,name="Grapes",price=100,measurement_unit="kg")
    i4 = p.Item(id=4,name="Milk",price=250,measurement_unit="litre")

    checkout1 = p.Cash_register(AWAIS)
    checkout2 = p.Cash_register(AHMED)

    checkout1.add_item(i1, 2,discount=10)
    checkout1.add_item(i2, 1)
    checkout2.add_item(i3, 1)
    checkout2.add_item(i4, 1)
    print("\n\n")
    checkout1.display_invoice()
    print("\n\n")
    checkout2.display_invoice()


    checkout1.update_item(i2, 5, 20)
    checkout2.update_item(i3, 5, 10)

    print("\n\n")
    checkout1.display_invoice()
    print("\n\n")
    checkout2.display_invoice()

    checkout1.remove_item("Eggs")

    checkout2.add_item(i3, 1)
    checkout2.add_item(i4, 1)
    print("\n\n")
    checkout1.display_invoice()
    print("\n\n")
    checkout2.display_invoice()


main()