def upper_lower():
	x = raw_input("put a sentence here:")
	dict = {"upper case": 0, "lower case" : 0}
	for i in range(len(x)):
		if x[i] == x[i].upper():
			dict["upper case"]+=1
		if x[i] == x[i].lower():
			dict["lower case"]+=1
		else:
			pass
	return dict

print(upper_lower())		
