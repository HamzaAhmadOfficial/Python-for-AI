class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        
        total = menu[flavor] * cups
        print(f"Your total bill for {cups} cups of {flavor} chai is: {total} PKR")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        print("Thank you for visiting our chai shop!")

bill("mint", 2)  # This will raise InvalidChaiError
bill("masala", "three")  # This will raise TypeError
bill("ginger", 3)  # This will work fine