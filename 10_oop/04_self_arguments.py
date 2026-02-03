class Chaicup:
    size = 150 # in ml

    def describe(self):
        return f"A {self.size}ml chai cup."
    
cup = Chaicup()
print(cup.describe())  # Output: A 150ml chai cup.
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))