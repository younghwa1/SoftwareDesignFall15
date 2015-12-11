""" 
Toolbox4: Revise MiniProject2
# created on Thu Dec 10 21:48 2015
# @author: YeongHwa Kim

I revised "build_random_function" and "evaluate_random_function".
"""
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

# Definition for random function building function
# Input: the possible range of the depth for function(int)
# Output: the list of functions(list)
def build_random_function(min_depth, max_depth):
	dep = random.randint(min_depth, max_depth)
		
	unit = [["x"], ["y"]]
	building_block = [["prod", ["a"], ["b"]], ["cos_pi", ["a"]], ["sin_pi", ["a"]]]

	if dep == 1:
		return random.choice(unit)
	else:
		outlist = random.choice(building_block)
		if outlist[0] == "cos_pi" or outlist[0] == "sin_pi" :
			dep = dep -1
			outlist[1] = build_random_function(1, dep)
			return outlist
		else:
			dep  = dep - 1
			outlist[1] = build_random_function(1, dep)
			outlist[2] = build_random_function(1, dep)
			return outlist

# Definition for evaluating function
# Input1: list of functions which wants to calculate(list)
# Input2: input value for x(float)
# Input3: input value for y(float) 
# Output: mathematically calculated value(float)
def evaluate_random_function(random_function, x, y):
	outer_function = random_function
	length = len(random_function)
	if length == 1:
		if outer_function[0] == "x":
			return X(x, y)
		elif outer_function[0] == "y":
			return Y(x, y)

	else:
		if outer_function[0] == "cos_pi":
			inner_function = outer_function[1]
			return cos_pi(evaluate_random_function(inner_function, x, y))
			
		if outer_function[0] == "sin_pi":
			inner_function = outer_function[1]
			return sin_pi(evaluate_random_function(inner_function, x, y))
			
		if random_function[0] == "prod": 
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
funcR = build_random_function(1, 8)
funcG = build_random_function(2, 4)
funcB = build_random_function(5, 9)

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
im.save('openplease.png')