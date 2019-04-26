#!/usr/bin/env python3

"""
Project Euler Problem 45
========================

Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

Triangle     T[n]=n(n+1)/2   1, 3, 6, 10, 15, ...
Pentagonal   P[n]=n(3n-1)/2  1, 5, 12, 22, 35, ...
Hexagonal    H[n]=n(2n-1)    1, 6, 15, 28, 45, ...

It can be verified that T[285] = P[165] = H[143] = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""

def triangle(num):
    return int(num * (num + 1) / 2) 


def pentagonal(num):
    return int(num * (3 * num - 1) / 2) 


def hexagonal(num):
    return int(num * (2 * num - 1))


def main():
    t_index = 286
    p_index = 165
    h_index = 143 

    while True:
        t_value = triangle(t_index)
        p_value = pentagonal(p_index)
        h_value = hexagonal(h_index)

        if t_value == p_value and t_value == h_value:
            print(t_value)
            break
        else:
            minimum = min([t_value, p_value, h_value])
            if minimum == t_value: t_index += 1
            elif minimum == p_value: p_index += 1
            else: h_index +=1


if __name__ == "__main__":
    main()
