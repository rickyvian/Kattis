n=int(raw_input())
value = 0
for i in range(0,n):
	terms = int(raw_input())
	power = terms%10
	real_terms = terms/10
	value += real_terms**power
print value
