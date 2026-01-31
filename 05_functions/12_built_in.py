def chai_flavor(flavor="masala"):
    """ Returns the flavor of chai."""
    chai = "ginger"
    return flavor

print(chai_flavor.__doc__)  # Accessing the docstring of the function
print(chai_flavor.__name__)  # Accessing the name of the function

# help(len)  # Using the built-in help function to get information about len function

def generate_bill(chai, samosa):
    """
    Calculates the total bill for chai and samosas
    :param chai: number of chai cups (10 rupees each)
    :param samosa: Number of samosa (15 rupees each)
    : return: total bill, thankyou message)
    """
    total = chai * 10 + samosa * 15
    return total, "Thank you for visiting!"

print(generate_bill.__doc__)

chai, samosa = 2, 3
print("Dear customer your bill is RS: ", generate_bill(chai, samosa)) # Calling the function to generate bill