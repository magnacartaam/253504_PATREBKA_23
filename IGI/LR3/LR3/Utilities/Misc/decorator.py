# Default decorator for all module business functions. Prints function name and all arguments with their values
def decorator_it(func):
    arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
    def wrapper(*args, **kwargs):
        print(f"Running function {func.__name__} from {func.__module__}() with: ")
        for i in range(0, len(arg_names)):
            print(f"\t{arg_names[i]} = {args[i]}")
        func(*args, **kwargs)
    return wrapper