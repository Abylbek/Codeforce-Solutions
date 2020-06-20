n = int(input())
pages =list(map(int , input().split()))
i = 0
sumofpages = 0
while sumofpages < n:
	if i == 7:
		i = 1
	else:
		i +=1
	sumofpages += pages[i - 1]
print(i)
