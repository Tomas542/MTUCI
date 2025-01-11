def Schitator(num1, num2, op):
    num1 = float(num1)
    num2 = float(num2)
    op = str(op)
    result = "hehe"

    if op == "div":
        if num2 == 0:
            result = "Error"

        else:
            result = num1 / num2

    elif op == "mul":
        result = num1 * num2

    elif op == "add":
        result = num1 + num2

    elif op == "sub":
        result = num1 - num2

    if result != "Error" and result != "hehe":

        if result // 1 == result:
            result = int(result)

    return result