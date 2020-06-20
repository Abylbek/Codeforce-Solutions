n , t = map(int , input().split())
queue = input.split()
queue_list = list(queue)
for i in range(t):
	i = 0
	while (i < n -1):
		if queue_list[i] == "B" and queue_list[i+1] == "G":
			queue_list[i] == "G"
			queue_list[i+1] == "B"
			i += 2;
		else:
			i+=1
result = "".join(queue_list)
print(result)