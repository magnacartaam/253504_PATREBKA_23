from Utilities.Misc.repeated_exec import run
from Tasks import (
    task_1,
    task_2,
    task_3,
    task_4,
    task_5,
)

# Lab Assignment №3 - v1.
# By Daniil I. Patrebka - 05.04.2024
# The program consists of task modules, which are passed in tuples into repeated exec function.
# In order for continuous input to work, each task module must contain launcher(*args, **kwargs) and
# input_and_start() functions. Module tuple structure is (module_name, module_cosmetic_name, module_description)

task_1_tuple = (task_1, "Task 1", "According to your assignment, you need to create a program to compute the value of a "
                            "function (asin) using a power series expansion. Set the calculation precision to eps. "
                            "Provide a maximum number of iterations equal to 500. Output the number of terms in the "
                            "series required to achieve the specified calculation precision.")

task_2_tuple = (task_2, "Task 2", "Organize a loop by counting numbers and summing their cubes. End of the cycle - enter the number 12")

task_3_tuple = (task_3, "Task 3", "[no regex] Determine whether the string entered from the keyboard is binary number.")

task_4_tuple = (task_4, "Task 4", """[no regex] a) determine the number of lowercase letters;
b) find the last word containing the letter 'i' and its number;
c) print the line excluding words starting with 'i'.""")

task_5_tuple = (task_5, "Task 5", "Find the number of list elements greater than the number C (parameter C is entered from the keyboard by the user) and the product of the list elements located up to the maximum modulo element.")

run([task_1_tuple, task_2_tuple, task_3_tuple, task_4_tuple, task_5_tuple])