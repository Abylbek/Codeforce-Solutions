n = int(input())
numbers = list(map(int, input().split()))
maxi = mini = numbers[0]
wow = 0
for i in numbers[1:]:
	if i < mini:
		wow+=1
		mini = i
	if i > maxi:
		wow+=1
		maxi = i
print(wow)
