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
    # Convert expression to list of tokens
    tokens = postfix_expression.split()

    # Create empty stack
    stack = []

    # Traverse tokens
    for token in tokens:
        # If token is an operand, push it onto stack
        if token.isnumeric():
            stack.append(int(token))
        # If token is an operator, pop top two operands from stack, apply operator, and push result onto stack
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)
        # If token is a function, pop top operand from stack, apply function, and push result onto stack
        elif token == "sqrt":
            operand = stack.pop()
            result = operators[token](operand)
            stack.append(result)

    # Final result is at top of stack
    return stack[-1]

print(evaluate_postfix("2 20 * 2 / 3 4 + 3 2 ^ * + 6 - 15 +"))
