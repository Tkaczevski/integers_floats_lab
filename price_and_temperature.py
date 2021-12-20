# Run the tests, then change the functions and test expectations
# The tests need to pass and the function needs to meet the requirements

def unit_price():
    # function requirements:
    # the user will input a price (¥), and a weight (kg). This function should return the price per kilogram
    price = int(input("What is the price? (¥) "))
    weight = int(input("What is the product weight? (kg) "))
    return f"This product is ¥{price/weight}/kg"


def celsius_to_fahrenheit():
    # function requirements:
    # the user will input a temperature in celsius. This function should return the temperature in Fahrenheit
    celsius = int(input("What's the temperature in °C? "))
    farenheit = (9 / 5) * celsius + 32
    return f"{celsius}°C is {farenheit}°F"
