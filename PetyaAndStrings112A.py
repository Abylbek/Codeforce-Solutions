first = input()
second = input()
if first.lower() == second.lower():
	print(0)
elif first.lower() > second.lower():
	print(-1)
else:
	print(1)