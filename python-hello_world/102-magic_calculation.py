#!/usr/bin/python3
def magic_calculation(a, b):
    result = 98  # LOAD_CONST 1 (98)
    result = result ** a  # LOAD_FAST 0 (a) + BINARY_POWER
    result = result + b  # LOAD_FAST 1 (b) + BINARY_ADD
    return result  # RETURN_VALUE

# Example usage
a = 3
b = 5
result = magic_calculation(a, b)
print("Result:", result)

