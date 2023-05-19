#!/usr/bin/env python3

# def print_fibonacci(length):
#     if length == 0:
#         print([])

#     elif length == 1:
#         print([0])

#     elif length == 2:
#         print([0,1])

#     elif length == 10:
#         print 


def print_fibonacci(length):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(length):
        fib_sequence.append(a)
        a, b = b, a + b
    print(fib_sequence)