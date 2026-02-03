class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)  # Output: hot

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing: ", cutting.temperature)  # Output: Mild
print("New attribute cup: ", cutting.cup)  # Output: small
print("Direct look into the class: ", Chai.temperature)  # Output: hot

del cutting.temperature
del cutting.cup
print("After deleting instance attribute: ", cutting.temperature)  # Output: hot
print("After deleting cup attribute", cutting.cup)  # Raises AttributeError
