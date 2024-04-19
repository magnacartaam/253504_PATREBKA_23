from Utilities.Input import sequence_input
from Utilities.Misc.decorator import decorator_it
from Utilities.Misc import divider

@decorator_it
def launch(data):
    """Launches task function."""
    output(raise_to3rd_pow(data))

def raise_to3rd_pow(seq):
    """Calculates the sum of all elements in sequence raised to the 3rd power."""
    result = 0
    for number in seq:
        result += number**3
    return result

def output(result):
    """Outputs task results."""
    print(f"Sum of elements to the third power: {result}")

def input_and_start():
    """Handles user input and calls function launcher."""
    print("\n\t1. Generate random numbers")
    print("\t2. Manual input")
    divider.print_secondary_divider()
    code = int(input("Enter option number: "))
    if code == 1:
        lower = int(input("\tChoose lower bound for number: "))
        upper = int(input("\tChoose upper bound for number: "))
        length = int(input("\tChoose length of number sequence: "))
        divider.print_main_divider()
        try:
            assert upper > lower
            assert length > 0
            launch(sequence_input.number_sequence_random(lower, upper, length))
        except AssertionError:
            print("Invalid input, try again\n")
            input_and_start()
    if code == 2:
        launch(sequence_input.number_sequence_manual(12))