def in_language(name):
	i = len(name)
	if i % 2 == 0 :
		ii= i/2
		ch1 = 'a' * (ii)
		ch2 = 'b' * (ii)
		if name[:ii] == ch1:
			if name[ii:] == ch2:
				return True
			else:
				return False
		elif i == 0:
			return True
		else:
			return False
	else:
		return False
