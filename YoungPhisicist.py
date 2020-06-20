n = int(input())
solution = [0,0,0]
for i in range(n):
	numbers = list(map(int , input().split()))
	solution[0] += numbers[0]
	solution[1] += numbers[1]
	solution[2] += numbers[2]
for num in solution:
	if num != 0:
		anwer = "NO"
		break
	else:
		anwer = "YES"
print(anwer)