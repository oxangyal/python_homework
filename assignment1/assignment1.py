# Write your code here.
def hello():
    return 'Hello!'

def greet(name):
    return f'Hello, {name}!'
greet("Oxana")

def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc(1, 5, "add"))
print(calc(10, 5, "subtract"))
print(calc(1, 5, "add"))
print(calc(10, 2, "power"))
print(calc(10, 2, "int_divide"))
print(calc(10, 0, "divide"))
print(calc(10, 3, "modulo"))
print(calc("one", "two", "multiply"))

def data_type_conversion(value, name):
    try:
        if name == "int":
            return int(value)
        elif name == "float":
            return float(value)
        elif name == "str":
            return str(value)
        else:
            return f"Unsupported data type: {name}"
    except ValueError:
        return f"You can't convert {value} into a {name}."

print(data_type_conversion("nonsense", "int"))
print(data_type_conversion(1, "int"))
print(data_type_conversion("nonsense", "str"))
print(data_type_conversion(10.5, "int"))
print(data_type_conversion(10.5, "float"))

def grade(*args):
    try:
        if not args:
            return "Invalid data was provided."
        average = sum(args) / len(args)
        if average >= 90:
           return "A"
        elif  average >= 80:
           return "B"
        elif  average >= 70:
           return "C"
        elif  average >= 60:
           return "D"
        else:
           return "F"
    except (TypeError, ValueError):
        return "Invalid data was provided."

print(grade(90, 87))
print(grade(90, "B", 87))