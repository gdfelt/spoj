#!/usr/bin/env python3

"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""



def main():
	for n in range(1, 30):
		for m in range(n + 1, 30):
			a = m*m - n*n
			b = 2 * m * n
			c = m*m + n*n
			if a + b + c == 1000:
				print(a*b*c)

if __name__ == "__main__":
	main()