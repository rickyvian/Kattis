d = []
while True:
	n = int(input())
	if(n <0):
		break
	ti = 0
	distance = 0
	for i in range (n) :
		s,tu = input().split()
		s,tu = [int(s),int(tu)]
		t = tu - ti
		ti = tu
		distance += s*t
	d.append(distance)

for i in range (len(d)):
	print(d[i], " miles")

