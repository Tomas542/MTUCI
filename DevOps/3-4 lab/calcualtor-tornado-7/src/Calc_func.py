def schitator(num1: float, num2: float, op: str) -> str:
    num1 = float(num1)
    num2 = float(num2)
    op = str(op)
    buffer_float = .0
    result = ""

    if op == "div":
        if num2 == 0:
            result = "Error"

        else:
            buffer_float = float(num1 / num2)

    elif op == "mul":
        buffer_float = float(num1 * num2)

    elif op == "add":
        buffer_float = float(num1 + num2)

    elif op == "sub":
        buffer_float = float(num1 - num2)

    if result != "Error":
        buffer_int = int(buffer_float)

        if buffer_float == buffer_int:
            result = str(buffer_int)
        else:
            result = str(buffer_float)

    return result
