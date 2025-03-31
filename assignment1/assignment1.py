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

def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result

print(repeat("word", 5))

def student_scores(position, **kwargs):

    if position == "best":
        max = 0
        max_name = ""
        for key, value in kwargs.items():
            if value > max:
               max = value
               max_name = key
        return max_name
    elif position == "mean":
        sum = 0

        for key, value in kwargs.items():
            sum += value

        return sum / len(kwargs)

print(student_scores("best", Oxana=1, David=2, Anna=5))
print(student_scores("mean", Oxana=1, David=2, Anna=5))

def titleize(string):
    words = string.split()
    little_words = {"a", "on", "an", "the", "and", "of", "is", "in"}
    words[0] = words[0].capitalize()
    words[-1] = words[-1].capitalize()

    for i in range(1, len(words) - 1):
        if words[i].lower() not in little_words:
            words[i] = words[i].capitalize()
        else:
            words[i] = words[i].lower()

    return " ".join(words)
print(titleize("petrovy in flu"))

def hangman(secret, guess):
    new_list = []
    for i in secret:
        if i in guess:
            new_list.append(i)
        else:
            new_list.append("_")
    return "".join(new_list)

print(hangman("alphabet", "ab"))
def pig_latin(string):
    words = string.split()
    result = ""
    vowels = "aeiou"

    for word in words:
        if word[0] in vowels:
            result += word + "ay"
        elif word[:2] == "qu":
            result += word[2:] + "quay"
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i:i+2] == "qu":
                    i += 2
                    break
                i += 1
            result += word[i:] + word[:i] + "ay"

        result += " "
    return result[:-1]

print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("cherry"))
print(pig_latin("square"))
print(pig_latin("long course season"))




