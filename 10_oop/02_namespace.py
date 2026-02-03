class Chai:
    origin = "Pakistan"

print(Chai.origin) # Accessing class variable without creating an instance

Chai.is_hot = True  # Adding a new class variable dynamically
print(Chai.is_hot) # Accessing the newly added class variable

# creating objects from the class Chai

masala = Chai()
print(f"Masala {masala.origin}") # Accessing class variable through an instance
print(f"Masala {masala.is_hot}") # Accessing dynamically added class variable through an instance

masala.is_hot = False

print("Class: ", Chai.is_hot) # Accessing class variable
print("Masala: ", masala.is_hot) # Accessing instance variable

masala.flavor = "spicy" # Adding an instance variable dynamically
print(masala.flavor) # Accessing the instance variable
