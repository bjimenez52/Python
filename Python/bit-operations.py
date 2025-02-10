
'''
Homework: bit-operations
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''
# Bitwise AND
a = 12  # In binary: 1100
b = 7  # In binary:  0111
result = a & b  # Bitwise AND
print(result)  # Output: 4 (Binary: 0100)

# Bitwise OR
a = 12  # In binary: 1100
b = 7  # In binary:  0111
result = a | b  # Bitwise OR
print(result)  # Output: 15 (Binary: 1111)

# Bitwise NOT
a = 12  # In binary:  0000 1100 
result = ~a
print(result)  # Output: -13

# Bitwise XOR
a = 12  # In binary:  1100
b = 7  # In binary:  0111
result = a ^ b  # Bitwise XOR
print(result)  # Output: 11 (Binary: 1011)

# Bitwise Left Shift
a = 12  # In binary: 0000 1100
result = a << 2
print(result)  # Output: 48 (Binary: 0011 0000)

# Bitwise Right Shift
a = 100  # In binary: 0110 0100
result = a >> 3
print(result)  # Output: 12 (Binary: 0000 1100)