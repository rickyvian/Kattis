L = int(input())
D = int(input())
X = int(input())
summ = 0
sumn = 0

def s(n):
	i = 1
	digits = []
	while(n//i) > 0:
		digits.append(int((n/i)%10))
	#	print(digits)
		i = i*10
	s = sum(digits)
	return s

while True:
	if(s(L) == X):
		print(L)
		break
	L+=1

while True:
	if(s(D) == X):
		print(D)
		break
	D-=1


