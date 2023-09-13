#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    if length > 0:
        sequence.append(0)
    if length > 1:
        sequence.append(1)

    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence  # Return the complete sequence


result = print_fibonacci(8)
print(result)




# [3,5,2,3,8,9,5]
   