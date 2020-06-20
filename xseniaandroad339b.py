n , m = map(int,  input().split())
numbers = list(map(int, input().split()))
cycle = 0
for i in range(m - 1):
	if numbers[i] > numbers[i+1]:
		cycle += 1
print(cycle*n + numbers[-1] - 1)