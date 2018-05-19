def chr_count():
	count = 0 
	x = raw_input("put in a sentence:")
	a = []
	for i in range(33, 127):
		a.append(chr(i))

	for i in range(len(x)-1):
		if x[i] in a:
			count += 1
	return count

print(chr_count())

