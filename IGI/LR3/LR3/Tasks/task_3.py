from Utilities.Input import text_input
from Utilities.Misc.decorator import decorator_it
from Utilities.Misc.divider import (
    print_main_divider,
    print_secondary_divider,
)

@decorator_it
def launch(data):
    """Launches task and calls output function."""
    is_binary = check_string(data)
    output(data, is_binary)

def check_string(text):
    """Checks if string contains only ones and zeroes."""
    binary ='01'
    counter = True
    for symbol in text:
        if symbol not in binary:
            counter = False
    return counter

def output(text, is_binary):
    """Performs task output."""
    if is_binary:
        print(f"\nThe string: '{text}'\nIS a binary number")
    else:
        print(f"\nThe string: '{text}'\nIS NOT a binary number")


def input_and_start():
    """Handles user input and calls function launcher."""
    print("\n\t1. Generate random lorem text")
    print("\t2. Manual text input")
    print_secondary_divider()
    code = int(input("Enter option number: "))
    print_main_divider()
    if code == 1:
        launch(text_input.text_input_random())
    if code == 2:
        launch(text_input.text_input_manual())