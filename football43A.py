n = int(input())
d = {}
names = []
for i in range(n):
	name = input()
	if name in d:
		d[name] = d[name] + 1
	else:
		d[name] = 1
		names.append(name)
if len(names) == 1:
	print(names[0])
elif d[names[0]] > d[names[1]]:
	print(names[0])
else:
	print(names[1])
