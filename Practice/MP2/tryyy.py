import random
from PIL import Image
import math

def prod(a, b):
	return float(ab)
def cos_pi(a):
	return float(math.cos(math.pi*a))
def sin_pi(a):
	return float(math.sin(math.pi*a))
def X(a, b):
	return float(a)
def Y(a, b):
	return float(b)


random_function = ['prod', ['cos_pi', ['cos_pi', ['x']]], ['sin_pi', ['cos_pi', ['x']]]]

def evaluate_random_function(random_function, x, y):
	outer_function = random_function
	if len(outer_function) == 1:
		if outer_function[0] == "x":
			return X(x, y)

		elif outer_function[0] == "y":
			return Y(x, y)

	else:
		if outer_function[0] == "cos_pi":
			inner_function = outer_function[1]
			if len(inner_function) == 1:
				if inner_function[0] == "x":
					inner_function[0] = X(x, y)
				elif inner_function[0] == "y":
					inner_function[0] = Y(x, y)
				in_put = inner_function[0]
				return cos_pi(in_put)
				
				 
			else:				
				outer_function = inner_function
				a = evaluate_random_function(outer_function, x, y)
				return cos_pi(a)

		if outer_function[0] == "sin_pi":
			inner_function = outer_function[1]
			if len(inner_function) == 1:
				if inner_function[0] == "x":
					inner_function[0] = X(x, y)
				elif inner_function[0] == "y":
					inner_function[0] = Y(x, y)
				in_put = inner_function[0]
				return sin_pi(in_put)
				
				
			else:
				outer_function = inner_function
				a = evaluate_random_function(outer_function, x, y)
				return sin_pi(a)
		
		if random_function[0] == "prod":
			inner_function1 = outer_function[1]
			inner_function2 = outer_function[2]
			a = evaluate_random_function(inner_function1, x, y)
			b = evaluate_random_function(inner_function2, x, y)
			return a*b
print evaluate_random_function(random_function, 1, 0)