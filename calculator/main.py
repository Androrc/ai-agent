# calculator/main.py

import sys
from pkg.calculator import Calculator
from pkg.render import format_json_output


def main():
    """
    CLI entry point for the Calculator app.
    Evaluates a mathematical expression passed as a command-line argument
    and prints the result in a formatted JSON-like output.
    """
    calculator = Calculator()
    
    # If no arguments provided, show usage instructions
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    # Join all command-line arguments to form the expression string
    expression = " ".join(sys.argv[1:])
    try:
        # Evaluate the expression using the Calculator class
        result = calculator.evaluate(expression)

         # Format the output before printing
        if result is not None:
            to_print = format_json_output(expression, result)
            print(to_print)
        else:

            # Handle empty or whitespace-only expressions
            print("Error: Expression is empty or contains only whitespace.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()