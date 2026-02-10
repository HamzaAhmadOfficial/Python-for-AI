class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, Sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Cannot make chai: missing ingredients. Milk or Sugar")
    print("Chai is ready!")