n = int(input())
finalresult = []
for i in range (n):
	inp = list(map(int,input().split()))
	if inp[1]-inp[0] == inp[2]:
		result = 1
		finalresult.append(result)
	if inp[1]-inp[0] > inp [2]:
		result = 2
		finalresult.append(result)
	if inp[1]-inp[0] < inp[2]:
		result = 3
		finalresult.append(result)

for i in range(n):
	if finalresult[i] == 1:
		print ("does not matter")
	if finalresult[i] == 2:
		print ("advertise")
	if finalresult[i] == 3:
		print ("do not advertise")
