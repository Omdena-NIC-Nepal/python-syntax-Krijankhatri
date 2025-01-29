def format_string(name: str, age: int) -> str:
    """
    Create a formatted string using f-strings.
    No error handling needed - simplest function.
    """
    return f"My name is {name} and I am {age} years old"


def conditional_check(number: int) -> str:
    """
    Check if a number is greater, lesser, or equal to 10.
    """
    try:
        if number == 10:
            return "Equal"
        elif number < 10:
            return "Lesser"
        else:
            return "Greater"
    except TypeError:
        return "Error: Input must be a number"


def loop_sum(n: int) -> int:
    """
    Calculate sum of numbers from 1 to n using a loop.
    """
    try:
        total = 0
        for i in range(n + 1):
            total += i
        return total
    except TypeError:
        return "Error: Input must be a whole number"


def list_operations(numbers: list) -> tuple:
    """
    Perform operations on a list of numbers.
    """
    try:
        return sum(numbers), max(numbers), min(numbers)
    except TypeError:
        return "Error: List must contain numbers"
    except ValueError:
        return "Error: List cannot be empty"


def dict_operations(students_dict: dict) -> list:
    """
    Find students with scores above 80.
    """
    try:
        return [name for name, score in students_dict.items() if score > 80]
    except AttributeError:
        return "Error: Input must be a dictionary"


def set_operations(list1: list, list2: list) -> set:
    """
    Find common elements between two lists.
    """
    try:
        return set(list1) & set(list2)
    except TypeError:
        return "Error: Both inputs must be lists"


def arithmetic_ops(a: float, b: float) -> dict:
    """
    Perform arithmetic operations.
    """
    try:
        return {
            "sum": a + b,
            "difference": a - b,
            "product": a * b,
            "quotient": a / b if b != 0 else "Error: Cannot divide by zero"
        }
    except TypeError:
        return "Error: Both inputs must be numbers"


def logical_ops(x: bool, y: bool) -> dict:
    """
    Perform logical operations.
    """
    return {
        "and": x and y,
        "or": x or y,
        "not_x": not x,
        "not_y": not y
    }


def bitwise_ops(a: int, b: int) -> dict:
    """
    Perform bitwise operations.
    """
    try:
        return {
            "and": a & b,
            "or": a | b,
            "xor": a ^ b
        }
    except TypeError:
        return "Error: Both inputs must be whole numbers"