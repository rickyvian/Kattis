n = int(input())
b = []
while n>0:
	b.append(n%2)
	n = int(n/2)
out = 0
i = len(b)
j = 0
while i > 0:
	if b[i-1] == 1:
		out += 2**j
	i -= 1
	j += 1
print(out)

