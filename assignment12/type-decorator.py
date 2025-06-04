# Task 2: A Decorator that Takes an Argument

def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Call the function and get the return value
            result = func(*args, **kwargs)
            # Convert the result to the specified type
            return type_of_output(result)
        return wrapper
    return decorator

# Define the functions
@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"

if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)

    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")  