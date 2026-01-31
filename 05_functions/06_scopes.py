def serve_chai():
    chai_type = "Masala" # local scope (Local scope is always inside a function)
    print(f"Inside function {chai_type}")


chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")


def chai_counter():
    chai_order = "lemon" # Enclosing scope
    def print_order():
        chai_order = "Ginger"
        print("Inner: ", chai_order)
    print_order()
    print("Outer: ", chai_order)

chai_order = "Tulsi" # Global 
chai_counter()
print("Global: ", chai_order)