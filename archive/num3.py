from package.array.array_stack import ArrayStack;
import operator

# Define operator precedence and associativity
precedence = {
    "^": (4, "right"),
    "sqrt": (4, "right"),
    "*": (3, "left"),
    "/": (3, "left"),
    "+": (2, "left"),
    "-": (2, "left"),
    "(": (1, "none"),
}

# Define operators and their corresponding functions
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
    "sqrt": operator.pow,
}

# Convert infix expression to postfix expression
def infix_to_postfix(s : str) -> str:
    print("Infix:", s)
    # Convert expression to list of tokens

    # Create empty stack and output list
    operators_stack = []; 
    postfix_expression = []
    
    # For two digit or more 
    previous_is_number = False

    # Traverse tokens
    for c in s:
        # If token is an operand, append it to output
        if c.isnumeric():
            if (previous_is_number):
                postfix_expression[-1] = postfix_expression[-1] + c
            else:
                postfix_expression.append(c)
                previous_is_number = True
        else:
            previous_is_number = False
            # If token is an operator or function
            if c in operators:
                # Pop operators off stack and append to output until lower-precedence operator is encountered
                while operators_stack and operators_stack[-1] != "(" and (precedence[c][0] < precedence[operators_stack[-1]][0] or (precedence[c][0] == precedence[operators_stack[-1]][0] and precedence[c][1] == "left")):
                    postfix_expression.append(operators_stack.pop())
                # Push token onto stack
                operators_stack.append(c)
            # If token is left parenthesis, push it onto stack
            elif c == "(":
                operators_stack.append(c)
            # If token is right parenthesis, pop operators off stack and append to output until left parenthesis is encountered
            elif c == ")":
                while operators_stack[-1] != "(":
                    postfix_expression.append(operators_stack.pop())
                operators_stack.pop()  # Discard left parenthesis

    # Pop any remaining operators off stack and append to output
    while operators_stack:
        postfix_expression.append(operators_stack.pop())

    # Join output list into space-separated string and return
    print("Postfix:", " ".join(postfix_expression))

infix_to_postfix("2*20/2+(3+4)*3^2-6+15")