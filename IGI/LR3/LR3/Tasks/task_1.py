import math
from Utilities.Misc.divider import print_main_divider
from Utilities.Misc.decorator import decorator_it

MAX_ITERATIONS = 500 # Maximum iterations limit.

def get_math_solution(x):
    """Calculates accurate arcsin(x) using standart math module."""
    return math.asin(x)

def get_series_solution(x, eps):
    """Calculates arcsin(x) using series formula for arcsin."""
    result = 0.0
    i = 0
    while True:
        if i > MAX_ITERATIONS:
            raise Exception(f"Iteration limit exceeded ({MAX_ITERATIONS})")
        if math.fabs(result - get_math_solution(x)) < eps:
            return (result, i)
        result += (math.factorial(2 * i) * x**(2*i + 1)) / (4**i * math.factorial(i)**2 * (2*i + 1))
        i+=1

def output(x, series_solv, math_solv, eps):
    """Outputs task results."""
    digits = int(math.log10(math.ceil(10 / eps)))
    f1 = f"{x}"
    f2 = f"{series_solv[1]}"
    f3 = f"{series_solv[0]: .{digits}f}"
    f4 = f"{math_solv: .{digits}f}"
    f5 = f"{eps}"
    print(f"{'x': <10}{'n': <10}{'F(x)': <15}{'Math F(x)': <15}{'eps': <10}")
    print(f"{f1: <10}{f2: <10}{f3: <15}{f4: <15}{f5: <10}")

@decorator_it
def launch(x, eps):
    """Launches task function."""
    assert math.fabs(x) < 1
    output(x, get_series_solution(x, eps), get_math_solution(x), eps)

def input_and_start():
    """Handles user input and calls function launcher."""
    x = float(input("\tEnter x (must be < 1): "))
    eps = float(input("\tEnter eps: "))
    print_main_divider()
    launch(x, eps)

    