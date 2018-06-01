n = int(input())
s = list(map(int, input().split()))
v = 0
d = []
for i in range (n):
	if s[i] >= 0:
		d.append(s[i])
#adding all items in the list d 
for j in d:
	v += j

print (v/len(d))
