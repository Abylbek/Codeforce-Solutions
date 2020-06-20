year = int(input())
while True:
	year += 1
	str(year)
	if len(set(year)) == 4:
		print(year)
		break