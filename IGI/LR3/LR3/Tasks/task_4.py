from Utilities.Input import text_input
from Utilities.Misc.decorator import decorator_it
from Utilities.Misc.divider import (
    print_main_divider,
    print_secondary_divider,
)

@decorator_it
def launch(data):
    """Launches task and calls output function."""
    point_a = count_lowercase_letters(data)
    point_b = find_last_word_starting_with_i(data)
    point_c = get_string_without_i_words(data)
    output(point_a, point_b, point_c)

def count_lowercase_letters(text):
    """Counts lower case letters."""
    return sum(map(str.islower, text))

def find_last_word_starting_with_i(text):
    """Returns last word starting with letter 'i' and its index."""
    words = get_words(text)
    searchable_word = ""
    index = 0
    for word in reversed(words):
        if word[0] == 'i':
            searchable_word = word
            index = words.index(word)
    return searchable_word, index

def get_string_without_i_words(text):
    """Returns text without words starting with the letter 'i'."""
    return " ".join([word for word in text.split() if not word[0]=='i' and not word[0]=='I'])

def get_words(text):
    """Returns words in lower case and without punctuation from given text."""
    words = text.split()
    return [word.rstrip(".,;:").lower() for word in words]


def output(point1, point2, point3):
    """Performs task output."""
    print(f"Count of letters in lower case: {point1}")
    print(f"Last word in text starting with the letter 'i' and word index: {point2[0]} : {point2[1]}")
    print(f"Given text without words starting with 'i': {point3}")


def input_and_start():
    """Handles user input and calls function launcher."""
    print("\n\t1. Generate random text")
    print("\t2. Manual text input")
    print("\t3. Default text")
    print_secondary_divider()
    code = int(input("Enter option number: "))
    print_main_divider()
    if code == 1:
        launch(text_input.text_input_random())
    if code == 2:
        launch(text_input.text_input_manual())
    if code == 3:
        launch(text_input.task_4_default_text())