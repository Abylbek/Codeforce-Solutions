s = input()
count = 0
for letter in s:
	if letter.islower():
		count += 1
if count < len(s)/2:
	print(s.lower())
else:
	print(s.upper())
