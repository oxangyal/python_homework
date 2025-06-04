
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

# Define the decorator
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        # Log function name
        logger.info(f"function: {func.__name__}")

        # Log positional parameters
        if args:
            logger.info(f"positional parameters: {args}")
        else:
            logger.info("positional parameters: none")

        # Log keyword parameters
        if kwargs:
            logger.info(f"keyword parameters: {kwargs}")
        else:
            logger.info("keyword parameters: none")

        # Call the function and get the return value
        result = func(*args, **kwargs)

        # Log the return value
        logger.info(f"return: {result}")

        return result
    return wrapper

# function 1: Simple function with no parameters
@logger_decorator
def hello_world():
    print("Hello, World!")

# function 2: Function with variable positional arguments
@logger_decorator
def variable_positional_args(*args):
    return True

# function 3: Function with variable keyword arguments
@logger_decorator
def variable_keyword_args(**kwargs):
    return logger_decorator

# Mainline code
if __name__ == "__main__":
    hello_world()
    variable_positional_args(1, 2, 3, "hello")
    variable_keyword_args(a=1, b=2, c="hello")