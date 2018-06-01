x = [1,1,2,2,2,8]
y = raw_input()
z = list(map(int,y.split()))
a = []
for i in range(6):
	a.append(x[i]-z[i])
	print a[i]
