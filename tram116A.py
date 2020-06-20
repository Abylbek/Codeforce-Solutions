n = int(input())
minimum = 0
total = 0
for i in range(n):
	out , enter = map(int , input().split())
	total = enter - out
	if total > minimum:
		minimum = total
print(minimum)
