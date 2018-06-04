l,f = list(map(int,input().split()))
if l != f:
	if l>f:
		n = (l*2)
	else:
		n = f*2
	print("Odd ", n)
elif l+f == 0:
	print ("Not a moose")
elif l == f:
	print("Even", l*2)
