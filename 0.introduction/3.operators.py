from fractions import Fraction

# Addition
print(2+3)

# Subtraction
print(5-2)

# Multiplication
print(3*8)

# Division
print(2/5)  # 0.4

# Floored Division
print(0//4)  # 0

# Power
print(2**4)

# Fraction
print(Fraction(1, 3))

# Bitwise xor
print(8 ^ 3)  # 11
# 1000  # 8 (binary)
# 0011  # 3 (binary)
# ----  # APPLY XOR ('vertically')
# 1011  # result = 11 (binary)


# In interactive mode, the last printed expression is assigned to the variable _. This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, for example:

# tax = 12.5 / 100
# price = 100.50
# price * tax
# 12.5625
# price + _
# 113.0625
# round(_, 2)
