n = int(input())
total = 0
for i in range(n):
	numbers = map(int , input().split())
	if sum(numbers) > 1:
		total+=1
print(total)