def tokenize(expression: str) -> list:
    number_symbols = [str(num) for num in range(10)] + ['.']
    operators = ['+', '-', '*', '/']
    unar_operators = ['+', '-']

    tokens = []
    current_number = ""
    last_is_number = False
    for element in expression:
        # We preserve character sequences if they represent a number
        if element in number_symbols:
            current_number += element
            last_is_number = True

        # If the element is an operator
        elif element in operators:
            # If what came before it was not a number
            if not last_is_number:
                # If the operator is unary
                if element in unar_operators:
                    # Then we add it to the sequence of numbers
                    current_number += element
                else:
                    # Then an unsuitable symbol is being used as a unary operator
                    raise ValueError("Invalid expression") 
                continue #Let's move on to the next element

            # If a saved sequence exists
            if current_number:
                # Add to the list of tokens and clear the sequence
                tokens.append(current_number)
                current_number = ""

            
            last_is_number = False
            tokens.append(element)

        # If we encounter a space
        elif element == " ":
            if current_number and last_is_number:
                tokens.append(current_number)
                current_number = ""

        else:
            # In the event of an unknown symbol, we output an error.
            raise ValueError("Invalid expression")
        
    # If any characters remain in the sequence, add them to the array of tokens.
    if current_number:
        tokens.append(current_number)
    
    return tokens



def validation(tokens: list) -> None:
    operators = ['+', '-', '*', '/']

    if not tokens:
        raise ValueError("Empty expression")

    last_is_number = False

    for current_token in tokens:
        if not last_is_number:
            try:
                float(current_token)
            except ValueError:
                raise ValueError("Invalid number")

            last_is_number = True

        else:
            if current_token not in operators:
                raise ValueError("Unknown operator")

            last_is_number = False

    if not last_is_number:
        raise ValueError("Invalid expression")

# Conversion to Reverse Polish Notation 
def to_rpn(tokens: list[str]) -> list:
    rpn = []
    stack_operators = []

    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }
    
    for i in range(len(tokens)):
        # all even are numbers, all odd are operators
        if i % 2 == 0:
            rpn.append(float(tokens[i]))
        else:
            # Pop from the stack and add to RPN
            while stack_operators and priority[stack_operators[-1]] >= priority[tokens[i]]:
                rpn.append(stack_operators[-1])
                stack_operators.pop()
            stack_operators.append(tokens[i])

    # Pop from the stack and add to RPN
    while stack_operators:
        rpn.append(stack_operators[-1])
        stack_operators.pop()

    return rpn

  
def calculation(expression: str) -> float:
    tokens = tokenize(expression)
    validation(tokens)
    tokens = to_rpn(tokens)

    calculation_stack = []

    for current_token in tokens:
        # If it is a number, we push it onto the stack.
        if isinstance(current_token, float):
            calculation_stack.append(current_token)
        else:
            # erform arithmetic operations on the top elements of the 
            second_number = calculation_stack.pop()
            first_number = calculation_stack.pop()

            if current_token == "+":
                calculation_stack.append(first_number + second_number)

            elif current_token == "-":
                calculation_stack.append(first_number - second_number)

            elif current_token == "*":
                calculation_stack.append(first_number * second_number)

            elif current_token == "/":
                if second_number == 0:
                    raise ValueError("Division by zero")
                calculation_stack.append(first_number / second_number)

    return calculation_stack.pop()




    
    
