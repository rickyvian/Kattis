n, w, h = raw_input().split()
n, w, h = [int(n), int(w), int(h)]
x = []

for i in range (0, n):
	l = int(raw_input())
	i += 1
	if l**2 <= w**2+h**2 :
		x.append("DA")
	else:
		x.append("NE")

for result in x:
	print result
	
