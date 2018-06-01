n = input()
t=[]
c=[]
g=[]
nt, nc, ng, small = [0, 0, 0,0]
for i in range (len(n)):
	if n[i] == 'T':
		t.append(n[i])
		nt += 1
	elif n[i] == 'C':
		c.append(n[i])
		nc += 1
	elif n[i] == 'G':
		g.append(n[i])
		ng += 1

output = len(t)**2+len(c)**2+len(g)**2

if nt > 0 and nc > 0 and ng > 0 :
	if nt<=nc and nt<=ng:
		small = nt
	elif nc<= nt and nc<=ng:
		small = nc
	elif ng<= nt and ng<= nc:
		small = ng
	
for i in range(small):
	output+=7
print(output)
