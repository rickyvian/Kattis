n = int(input())
school_list = []
team_list = []
for i in range(n):
	school_team = input().split()
	new_list = [elem for elem in scholl_team if 
	#new_list = [elem for elem in school_list if school_list.count(elem)==1]
	new_list = list(set(school_list))
print(new_list)
