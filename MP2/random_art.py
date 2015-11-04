<<<<<<< HEAD
# MiniProject 2
# created on Fri Oct 09 14:59:32 2015
# @author: YeongHwa Kim

import random 
from PIL import Image
import math


# Definition for the calculating unit functions
# Input and Output: numbers(float)

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

# Definition for the additional function.
# It used in "build_random_function(min_depth, max_depth)", for "prod"
# Because it's impossible to use "recursion" in for loops
# Input: depth(int) in between "min_depth" and "max_depth"
#		 this value is automatically choosed in the "build_random_function"
# Output: the functions list composed of only "sin_pi" and "cos_pi" (list)
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


# Definition for random function building function
# Input: the possible range of the depth for function(int)
# Output: the list of functions(list)
def build_random_function(min_depth, max_depth):
	dep = random.randint(min_depth, max_depth)
	flist = [] # Output
	
	# Make the standard: how to choose the function
	rn1 = random.random()  # I used random number
		
	if dep == 1:
		# only 'x' or 'y' can be a function for each of the 50% percentages
		if 0<= rn1 <0.5:
			flist.append("x")
		else:
			flist.append("y")
				
	else:
		# start from the deepest list, it should be ['x'] or ['y']
		if 0<= rn1 <0.5:
			flist.append("x")
		else:
			flist.append("y")
		# and then make outer list step by step
		for i in range(dep):
			rn = random.random() # make the standard only for this for loop
			newlist = [] # temporary outer function list
			
			# 'prod', 'cos_pi', and 'sin_pi' can be a function about 33.33% percentages for each
			if 0 <= rn < 0.3333:
				newlist.append("prod")
				# "prod" should have 2 functions which have the lower depth
				dep2 = dep - 1
				# to call 2 functions, using "use_for" function
				flist1 = ["a"]
				flist1[0] = use_for(dep2)
				flist2 = ["a"]
				flist2[0] = use_for(dep2)					

				newlist.append(flist1[0])
				newlist.append(flist2[0])
				flist = newlist # temporary outer function become the output
				
			elif 0.3333 <= rn < 0.6666:
				newlist.append("cos_pi")
				newlist.append(flist)
				flist = newlist
				
					
			else:
				newlist.append("sin_pi")
				newlist.append(flist)
				flist = newlist
				
				
	return flist	


# Definition for evaluating function
# Input1: list of functions which wants to calculate(list)
# Input2: input value for x(float)
# Input3: input value for y(float) 
# Output: mathematically calculated value(float)
def evaluate_random_function(random_function, x, y):
	# If outer_function's depth is n, then inner_function's depth is (n-1)
	outer_function = random_function

	if len(outer_function) == 1:
		if outer_function[0] == "x":
			return X(x, y)
		elif outer_function[0] == "y":
			return Y(x, y)

	else:
		# until program find the specific value(that time, inner_function's length should be 1)
		# do recursion
		# If the inner_function's length becomes 1, calculate the value with using unit functions
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
			# "prod" has 2 inner_functions
			inner_function1 = outer_function[1]
			inner_function2 = outer_function[2]
			a = evaluate_random_function(inner_function1, x, y)
			b = evaluate_random_function(inner_function2, x, y)
			return a*b


# Definition for interval remapping function
# Input1: the value that want to remap in different interval(float)
# Input2: the value that initial interval starts(float)
# Input3: the value that initial interval ends(float)
# Input4: the value that changed interval starts(float)
# Input5: the value that changed interval ends(float)
# Output: remapped "val"
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, ouput_interval_end):
	a = float(output_interval_start)
	b = float(val - input_interval_start)
	c = float(ouput_interval_end - output_interval_start)
	d = float(input_interval_end - input_interval_start)
	lol = a+b*c/d
	return lol


# Making RGB value

# Make random function for the R, G, B values
# If the depth goes high, the absolute value of the calculating results is going very small.
# So this program recognizes the output as 0 always, and it makes the one-colored pictures.
funcR = build_random_function(1, 3)
funcG = build_random_function(2, 4)
funcB = build_random_function(1, 2)

# lists of x, y values in range from -1 to 1
x_values = []
for i in range(350):
	a = remap_interval(i, 0, 350, -1, 1)
	x_values.append(a)

y_values = []
for i in range(350):
	a = remap_interval(i, 0, 350, -1, 1)
	y_values.append(a)

# Definition of function that calculate the RGB values
# Input: the x, y coordinates(int)
# Output: RGB value(tuple)
def extractRGB(i, j):
	R = evaluate_random_function(funcR, x_values[i], y_values[j])
	R = int(remap_interval(R, -1, 1, 0, 255))
	G = evaluate_random_function(funcG, x_values[i], y_values[j])
	G = int(remap_interval(G, -1, 1, 0, 255))
	B = evaluate_random_function(funcB, x_values[i], y_values[j])
	B = int(remap_interval(B, -1, 1, 0, 255))
	return R, G, B

# Make the image
im = Image.new("RGB", (350, 350))
for i in range(350):
	for j in range(350):
		im.putpixel((i, j),extractRGB(i, j))
im.save('openplease7.png')
=======
# -*- coding: utf-8 -*-
"""
Random_art.py

@author: amonmillner, adapted from pruvolo work
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image

def build_random_function(min_depth, max_depth):
    """ your doc string goes here
    """

    # your code goes here

def evaluate_random_function(f, x, y):
    """ your doc string goes here
    """

    # your code goes here

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """
    # your code goes here
    


#your additional code and functions go here
>>>>>>> 31d671e5a17071486f0485c43b98271c1708f511
