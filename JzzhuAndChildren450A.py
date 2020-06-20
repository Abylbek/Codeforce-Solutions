n , m = map(int , input().split())
numbers = list(map(int , input().split()))
maxchild = 0
need = 0
for index , num in enumerate(numbers):
	if num >= maxchild:
		maxchild = num
		need = index
print(need)
		