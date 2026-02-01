favorite_chai = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favorite_chai}
print(unique_chai)


recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elachi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)