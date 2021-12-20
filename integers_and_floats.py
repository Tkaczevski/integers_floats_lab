# Run the tests, then change the functions and test expectations
# The tests need to pass and the function needs to meet the requirements

def integer_division():
    # function requirements: divide the two integers and return the type of the result
    integer_1 = 20
    integer_2 = 4
    return type(integer_1/integer_2)


def float_integer_multiplication():
    # function requirements: multiply a float and integer and return the type of the result
    float_1 = 5.9
    integer_1 = 22
    return type(float_1*integer_1)


def inputs_are_strings():
    # function requirements: convert inputs from strings to divide any two numbers (integers or floats)
    fav_number_1 = int(input("What's your favorite number? "))
    fav_number_2 = float(input("What's your other favorite number? "))
    return type(fav_number_1 / fav_number_2)
