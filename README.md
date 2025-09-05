Custom Fraction Data Type in Python
This project implements a custom fractions class in Python to represent and manipulate rational numbers (fractions) with full arithmetic, comparison, and utility support.

Features:
Basic Arithmetic Operations: Addition, subtraction, multiplication, and true division with operator overloading.
Reflected Operators: Support mixed-type arithmetic where the fraction may be the right operand (e.g., 1 + fraction).
Comparisons: Equality and relational comparisons (==, !=, <, <=, >, >=) with integers, floats, and other fraction instances.
Normalization: Automatic simplification of fractions to their lowest terms.
Negation and Absolute Value: Support for unary negation and absolute value operations.
Type Conversions: Conversion between floats and fractions.
Reciprocal: Method to compute the reciprocal of a fraction.
Mixed Fraction Representation: Convert improper fractions to mixed fractions.
Parsing Utilities: Convert strings and integers to fraction instances.
Error Handling: Proper handling for invalid operations such as division by zero.

Usage Examples:
from fractions import fractions

# Create fraction instances
frac1 = fractions(4, 5)
frac2 = fractions(3, 4)

# Arithmetic
print(frac1 + frac2)   # Output: 31/20
print(frac1 - frac2)   # Output: 1/20
print(frac1 * frac2)   # Output: 12/20
print(frac1 / frac2)   # Output: 16/15

# Comparisons
print(frac1 == fractions(8, 10))  # True
print(frac1 < 1)                  # True
print(frac1 > 0.5)                # True

# Negation and absolute value
print(-frac1)                     # -4/5
print(abs(-frac1))                # 4/5

# Conversion to float
print(float(frac1))               # 0.8

# Reciprocal
print(frac1.reciprocal())        # 5/4

# Mixed fraction
print(frac1.mixed_fraction())    # 0 4/5

# Parsing from string
frac3 = fractions.str_to_frac("7/8")
print(frac3)                     # 7/8

Installation
No external dependencies are required. The class uses Python standard libraries only.

How to Run
Save the fractions.py file containing the class definition. Import and use it in your Python scripts as demonstrated in the usage examples.


