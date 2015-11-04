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

def use_for(dep):
	flist = []
	
	rn1 = random.random()
	if dep == 1:
		if 0<= rn1 <0.5:
			flist.append("x")
		else:
			flist.append("y")
				
	else:
		if 0<= rn1 <0.5:
			flist.append("x")
		else:
			flist.append("y")
		
		for i in range(dep):
			rn = random.random()
			newlist = []
			if 0 <= rn < 0.5:
				newlist.append("cos_pi")
				newlist.append(flist)
				flist = newlist
				
					
			else:
				newlist.append("sin_pi")
				newlist.append(flist)
				flist = newlist
				
				
	return flist	


def build_random_function(min_depth, max_depth):
	dep = random.randint(min_depth, max_depth)
	flist = []
	
	rn1 = random.random()
	if dep == 1:
		if 0<= rn1 <0.5:
			flist.append("x")
		else:
			flist.append("y")
				
	else:
		if 0<= rn1 <0.5:
			flist.append("x")
		else:
			flist.append("y")
		
		for i in range(dep):
			rn = random.random()
			newlist = []
			if 0 <= rn < 0.3333:
				newlist.append("prod")
				dep2 = dep - 1
				
				flist1 = ["a"]
				flist1[0] = use_for(dep2)
				flist2 = ["a"]
				flist2[0] = use_for(dep2)					

				newlist.append(flist1[0])
				newlist.append(flist2[0])
				flist = newlist
				
			elif 0.3333 <= rn < 0.6666:
				newlist.append("cos_pi")
				newlist.append(flist)
				flist = newlist
				
					
			else:
				newlist.append("sin_pi")
				newlist.append(flist)
				flist = newlist
				
				
	return flist	
		
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

print evaluate_random_function(build_random_function(3, 6), -1, 1)

print build_random_function(2, 5)
funcG = build_random_function(3, 30)
funcB = build_random_function(4, 35)