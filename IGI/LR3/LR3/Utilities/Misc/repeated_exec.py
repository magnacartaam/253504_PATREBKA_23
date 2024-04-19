import traceback
from Utilities.Misc.divider import (
    print_main_divider,
    print_secondary_divider,
)

def run(tasks):
    while True:
        print("\nChoose task: \n")
        print_options(tasks)
        chosen_task = get_user_input()
        if chosen_task == 'q' or chosen_task == 'Q':
            break
        try:
            tasks[chosen_task-1][0].input_and_start()
        except IndexError:
            print('[EXC] - NO such variant')
        except AssertionError:
            print('[EXC] - Invalid input, read task input limitations')
        except ValueError:
            print('[EXC] - Invalid input')
        except Exception as exc:
            print(f'[EXC] - {exc}')
            print(traceback.format_exc())
        finally:
            print_main_divider()
            key = input("Press any key to continue or press 'q' to quit: ")
            if key == 'q' or key == 'Q':
                break

def print_options(tasks):
    for task_info in tasks:
        print(f"{tasks.index(task_info)+1}. {task_info[1]}: {task_info[2]}")

def get_user_input():
    print_secondary_divider()
    return int(input("Enter task number or quit by pressing 'q': "))