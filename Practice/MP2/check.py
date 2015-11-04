import random
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

print use_for(3)