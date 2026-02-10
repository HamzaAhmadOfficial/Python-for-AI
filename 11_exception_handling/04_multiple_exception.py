def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print(f"Sorry that chai is not on new menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger", 2)
process_order("masala", "two")