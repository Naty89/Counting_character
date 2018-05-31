def say_number():
	o = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"}
	t = {2:"twenty", 3:"thirty", 4:"fourty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}
	h = {1:"one hundred", 2:"two hundred", 3:"three hundred", 4:"four hundred", 5:"five hundred", 6:"six hundred", 7:"eight hundred", 8:"eight hundred", 9:"nine hundred"}
	th = {1:"one thousand", 2:"two thousand", 3:"three thousand", 4:"four thousand", 5:"five thousand", 6:"six thousand", 7:"seven thousand", 8:"eight thousand", 9:"nine thousand"}
	m = {1:"one million", 2:"two million", 3:"three million", 4:"four million", 5:"five million", 6:"six million", 7:"seven million", 8:"eight million", 9:"nine million"}
	p = raw_input("Pick a number from 20 through 999,999,999 with no commas:")
	for k in range(len(p)-1):
		if len(p) == 1:
			i = o[int(p[0])]
		if len(p) == 2:
			i = t[int(p[0])] + " " + o[int(p[1])]
		if len(p) == 3:
			i = h[int(p[0])] + " " + t[int(p[1])] + " " + o[int(p[2])]
		if len(p) == 4:
			i = th[int(p[0])] + " " + h[int(p[1])] + " " + t[int(p[2])]+ " " + o[int(p[3])]
		if len(p) == 5:
			i = t[int(p[0])] + " " + th[int(p[1])] + " " + h[int(p[2])]+ " " + t[int(p[3])] + " " + o[int(p[4])]
		if len(p) == 6:
			i = h[int(p[0])] + " " + t[int(p[1])] + " " + th[int(p[2])]+ " " + h[int(p[3])] + " " + t[int(p[4])] + " " + o[int(p[5])]
		if len(p) == 7:
			i = m[int(p[0])] + " " + h[int(p[1])] + " " + t[int(p[2])]+ " " + th[int(p[3])] + " " + h[int(p[4])] + " " + t[int(p[5])] + " " + o[int(p[6])]
		if len(p) == 8:
			i = t[int(p[0])] + " " + m[int(p[1])] + " " + h[int(p[2])]+ " " + t[int(p[3])] + " " + th[int(p[4])] + " " + h[int(p[5])] + " " + t[int(p[6])] + " " + o[int(p[7])]
		if len(p) == 9:
			i = h[int(p[0])] + " " + t[int(p[1])] + " " + m[int(p[2])]+ " " + h[int(p[3])] + " " + t[int(p[4])] + " " + th[int(p[5])] + " " + h[int(p[6])] + " " + t[int(p[7])] + " " + o[int(p[8])]
	return i

print(say_number())
			
					
		


