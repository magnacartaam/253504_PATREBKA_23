import math
from Utilities.Input import sequence_input
from Utilities.Misc.decorator import decorator_it
from Utilities.Misc import divider

@decorator_it
def launch(data, parameter):
    """Launches task function."""
    output(amount_bigger_than_parameter(data, parameter),
           product_of_elements_before_max(data))

def amount_bigger_than_parameter(seq, parameter):
    """Calculates the amount of elements bigger than parameter."""
    return sum(True for el in seq if el > parameter)

def product_of_elements_before_max(seq):
    """Returns the product of list elements
       located before the max element by module."""
    max_index = seq.index(max(seq, key= lambda x: math.fabs(x)))
    product = 1
    for i in range(max_index):
        product *= seq[i]
    return product


def output(amount, product):
    """Outputs task results."""
    print(f"Amount of elements bigger than parameter: {amount}")
    print(f"Product of list elements located before the max element by module: {product}")

def input_and_start():
    """Handles user input and calls function launcher."""
    parameter = float(input("Enter parameter C: "))
    print("\n\t1. Generate random numbers")
    print("\t2. Manual input")
    divider.print_secondary_divider()
    code = int(input("Enter option number: "))
    if code == 1:
        lower = float(input("\tChoose lower bound for number: "))
        upper = float(input("\tChoose upper bound for number: "))
        length = int(input("\tChoose length of number sequence: "))
        divider.print_main_divider()
        try:
            assert upper > lower
            assert length > 0
            launch(sequence_input.number_sequence_random(lower, upper, length, is_float=True), parameter)
        except AssertionError:
            print("Invalid input, try again\n")
            input_and_start()
    if code == 2:
        length = int(input("\tChoose length of number sequence:"))
        launch(sequence_input.number_sequence_manual_with_length(length), parameter)