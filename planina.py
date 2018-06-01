iteration = int(raw_input())

multiplier = 1
dots = 3

if iteration == 1:
	dots = 3

else:
	for i in range(0,iteration-1):
		multiplier = multiplier*2

		dots += multiplier

print dots**2
