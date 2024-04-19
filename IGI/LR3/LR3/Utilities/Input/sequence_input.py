import random

def number_sequence_manual_with_length(length):
    input_sequence = []
    member = 0
    while length:
        member = float(input(f"Enter float: "))
        input_sequence.append(member)
        length -= 1
    return input_sequence

def number_sequence_manual(stop_code, is_float=False):
    input_sequence = []
    member = 0
    while member != stop_code:
        if is_float:
            member = float(input(f"Enter float or enter '{stop_code}' to stop: "))
        else:
            member = int(input(f"Enter integer or enter '{stop_code}' to stop: "))
        input_sequence.append(member)
    return input_sequence

def number_sequence_random(lower, upper, length, is_float=False):
    input_sequence = []
    for i in range(0, length):
        if is_float:
            input_sequence.append(random.uniform(lower, upper))
        else:
            input_sequence.append(random.randint(lower, upper))
    return list(input_sequence)