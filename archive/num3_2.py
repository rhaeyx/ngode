from package.array.array_stack import ArrayStack;

# Define operators and their corresponding functions
import operator

# Define operators and their corresponding functions
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
    "sqrt": operator.pow,
}

def evaluate_postfix(postfix_expression):
    # Convert expression to list of items
    items = postfix_expression.split()

    # Create empty stack
    stack = ArrayStack()

    # Traverse tokens
    for item in items:
        # If token is an operand, push it onto stack
        if item.isnumeric():
            stack.push(int(item))
        # If token is an operator, pop top two operands from stack, apply operator, and push result onto stack
        elif item in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[item](operand1, operand2)
            if (item == "sqrt"):
                result = operators[item](operand1, 1/2)

            stack.push(result)
        # If token is a function, pop top operand from stack, apply function, and push result onto stack
        elif item == "sqrt":
            operand = stack.pop()
            result = operators[item](operand)
            stack.push(result)

    # Final result is at top of stack
    return(float(stack.pop()))

print(evaluate_postfix("2 20 * 2 / 3 4 + 3 2 ^ * + 6 - 15 +"))
