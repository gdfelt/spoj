#!/usr/bin/env python3

"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

import utils

abundant_list = []
sum_abundant = set()

def check_if_sum(num):
	for x in abundant_list:
		if num - x <= 0:
			return False
		if num - x in abundant_list:
			return True
	return False

def main():
	
	# build abundant number list
	for x in range(12, 28123+1):
		if sum([ n for n in utils.get_factors(x)[:-1]]) > x:
			abundant_list.append(x)
			for num in abundant_list:
				sum_abundant.add(x + num)
	running_sum = 0
	for x in range(1, 28123+1):
		if x not in sum_abundant:
			running_sum += x
	


	print(running_sum)

if __name__ == "__main__":
	main()