megabyte = int(raw_input())
n = int(raw_input())
count = 0
new_megabyte = megabyte
while(count<n):
	used = int(raw_input())
	new_megabyte -= used
	new_megabyte += megabyte
	count += 1
print new_megabyte
