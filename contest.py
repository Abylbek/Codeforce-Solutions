n = int(input())
date1 = []
date2 = []
last = 0
for i in range(n):
	a , b = map(int, input().split())
	date1+=a
	date2+=b
date1.sort()
date2.sort()
for i in range(n):
	if date2[i] >= last:
		last = date2[i]
	else:
		last = date1[i]
print(last)