chai_menu = {
    "Masala Chai": 30,
    "Ginger Chai": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("The specified key that you are trying to access does not exists in the dictionary.")

print("Hello Chai Code") 