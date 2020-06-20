t = int(input())
for i in range(t):
	num = int(input())
	if (num/2)%2 == 1:
		print("NO")
	else:
		print("YES")
		array1 = []
		for i in range(2 , num + 1 , 2):
			array1.append(i)
		array2 = array1.copy()
		for i in range(array2//2):
			array2[i]-=1
		for i in range(array2//2,array2)
			i+=1
	print(array1)
	print(array2)



