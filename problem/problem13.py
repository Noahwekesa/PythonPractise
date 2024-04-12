"""
Problem 13: Write a program add.py that takes 2 numbers
as command line arguments and prints its sum.
"""

import sys

if len(sys.argv) > 2:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print("sum = %d" % (a + b))
    except ValueError:
        print("Failed to parse all aguments as integers.")
        exit(1)
else:
    print("Not enough numbers to add")
