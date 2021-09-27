#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	return [max(l) for l in numbers]

def join_integers(numbers):
	str_nbrs = ""
	for i in numbers:
		str_nbrs += str(i)
	# ou : return int("".join([str(n) for n in numbers]))
	return int(str_nbrs)

def generate_prime_numbers(limit):
	primes = []
	nombre = [i for i in range(2, limit + 1)]
	while len(nombre) != 0:
		primes.append(nombre[0])
		nombre2 = []
		for elem in nombre:
			if elem % nombre[0] != 0:
				nombre2.append(elem)
		nombre = nombre2
	return primes

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	result = []
	for i in range(1, num_combinations + 1):
		for s in strings:
			if excluded_multiples is None or i % excluded_multiples != 0:
				result.append(s + str(i))
	return result

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
