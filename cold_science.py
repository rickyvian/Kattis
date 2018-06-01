n = int(raw_input())
check = 0
temp = []
#for i in range(n):
temp = raw_input()
x = list(map(int,temp.split()))
j=0
for i in range(len(x)):
	if x[j] < 0:
		check += 1
	j+=1
print check
