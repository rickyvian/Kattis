n = int(input())
cities = []
b = []
for i in range (n):
	numCities = int(input())
	cities = []
	for i in range(numCities):
		cities.append(input())
	a = len(set(cities))
	b.append(a)
for i in range(len(b)):
	print(b[i])
