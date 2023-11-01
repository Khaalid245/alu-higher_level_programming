#!/usr/bin/python3

for char in range(ord('z'), ord('a') - 1, -1):
    print(chr(char) if (char - ord('z')) % 2 == 0 else chr(char).upper(), end='')

print()  # Add a newline after printing the characters

