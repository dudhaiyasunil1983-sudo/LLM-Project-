from langchain import tool

@tool

def multiply_numbers(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b

print(multiply_numbers.invoke({"a": 3, "b": 4}))
