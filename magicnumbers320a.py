def magic(n):
	length = len(n)
	index = 0
	while index<length:
		if n[index] == "1":
			index+=1
		elif (n[index] == "1") and (n[index + 1] == "4") and n-index >= 2:
			index+=1
		elif n[index]=="1" and n[index + 1]=="4" and n[index + 2]=="4" and n-index >= 3:
			index+=2
		else:
			return "NO"
	return "YES"
n = input()