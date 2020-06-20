n = int(input())
soldats = list(map(int , input().split()))
minimum = soldats[1] - soldats[0]
first , second = 0 , 1
for i in range(n - 1):
	for j in range(i+1,n):
		print(abs(soldats[j] - soldats[i]))
		if minimum >= abs(soldats[j] - soldats[i]):
			minimum = abs(soldats[j] - soldats[i])
			first = i
			second = j
			print("ans" + str(first+1) + " " + str(second+1))
