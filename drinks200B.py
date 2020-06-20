n = int(input())
numbers = map(int , input().split())
total = 0
for i in numbers:
	total += i/100
print(total/n*100)