# calculator/pkg/render.py

import json


def format_json_output(expression: str, result: float, indent: int = 2) -> str:
    """
    Formats a calculator expression and its result as a JSON string.
    
    Converts float results that are whole numbers into integers for cleaner output.
    """
    # Convert floats with no decimal part to int
    if isinstance(result, float) and result.is_integer():
        result_to_dump = int(result)
    else:
        result_to_dump = result

    # Prepare the dictionary to be serialized
    output_data = {
        "expression": expression,
        "result": result_to_dump,
    }
    # Return pretty-printed JSON string
    return json.dumps(output_data, indent=indent)