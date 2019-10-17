n=1000
ls_prime=[]
for i in range(1,n):
	divisible = 0
	for j in range(2,int(i/2+1)):
		if i%j == 0:
			divisible=1
	if divisible==0:
		ls_prime.append(i)
print(ls_prime)
