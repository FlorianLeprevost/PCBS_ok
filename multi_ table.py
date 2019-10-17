chiffres = [1,2,3,4,5,6,7,8,9]
for i in chiffres:
	for j in [i*k for k in chiffres]:
		'{:3}'.format(j)