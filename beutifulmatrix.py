for i in range(5):
	n = map(int  , input().split())
	for j in range(5):
		if j == 1:
			r = i
			c = j
			print(r)
			print(c)
print(abs(r - 2) +  abs(c - 2))