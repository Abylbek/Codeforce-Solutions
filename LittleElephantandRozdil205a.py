n = int(input())
numbers = list(map(int , input().split()))
if numbers.count(min(numbers)) > 1:
	print("stil")
else:
	print(numbers.index(min(numbers))