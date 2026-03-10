import random
from shlex import join


def get_pincodes(count):
    pins = []

    for _ in range(count):
        # Generates a 4-digit number and converts to string with leading zeros
        new_pin = f"{random.randint(0, 9999):04}"
        pins.append(new_pin)
        #print("\n".join(pins))
        #print(type(new_pin))
    return pins


# This block ensures the code runs only when the script is executed directly
if __name__ == "__main__":
    #number_of_pins = int(input("How many PIN codes you want?: "))
    number_of_pins = 50
    result = get_pincodes(number_of_pins)

    print(f"Generated Pins: {result}")
