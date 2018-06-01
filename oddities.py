n = int(input())
arr = []
for i in range(n):
	inp = int(input())
	arr.append(inp)
for j in range (n):
	if arr[j] %2 == 0:
		print (arr[j], "is even")
	else:
		print (arr[j], "is odd")
	j+=1
