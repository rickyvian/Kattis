word = input()
hiss = False
i = 1
for i in range(len(word)-1):
	if word[i] == 's':
		if word[i-1] == word[i]:
			hiss = True

if hiss == False:
	print("no hiss")
else:
	print("hiss")
