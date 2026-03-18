# calculator/pkg/calculator.py

class Calculator:
    """
    Simple calculator supporting +, -, *, / with operator precedence.
    Evaluates expressions in infix notation using two stacks.
    """
    def __init__(self):
        # Mapping of supported operators to their lambda implementations
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        # Operator precedence levels (higher number = higher precedence)
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression):
        """
        Public method to evaluate a mathematical expression string.
        Returns a float result or None if the expression is empty/whitespace.
        """
        if not expression or expression.isspace():
            return None
        # Tokenize expression by whitespace
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens):
        """
        Evaluate an infix expression given as a list of tokens.
        Uses two stacks: one for values, one for operators.
        """
        values = []
        operators = []

        for token in tokens:
            if token in self.operators:
                # Apply operators from the stack based on precedence
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        # Apply remaining operators
        while operators:
            self._apply_operator(operators, values)

        # After evaluation, there should be exactly one value left
        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        """
        Pop an operator and the last two values from their stacks, 
        apply the operator, and push the result back onto the values stack.
        """
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        # Apply the operator and push the result
        values.append(self.operators[operator](a, b))