#!/usr/bin/python3
def remove_char_at(s, n):
    # Check for invalid indices and return the original string
    if n < 0 or n >= len(s):
        return s
    # Remove the character at index n by slicing the string
    return s[:n] + s[n+1:]

# Test cases
print(remove_char_at("Chicago", 3))  # Output: "Chcago"
print(remove_char_at("Chicago", 15))  # Output: "Chicago"
print(remove_char_at("", 4))  # Output: ""
print(remove_char_at("Chicago", -3))  # Output: "Chicago"
print(remove_char_at("Chicago", 0))  # Output: "hicago"

