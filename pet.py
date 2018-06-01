summ = 0
fsumm = 0
number = 0
for i in range (5):
	n = list(map(int,input().split()))
	summ = sum(n)
	if summ > fsumm:
		fsumm = summ
		number = i+1
print(number, fsumm)
