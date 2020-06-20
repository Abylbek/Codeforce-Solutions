first = input()
second = input()
ans =""
for a, b in zip(list(x for x in first), list(y for y in second)):
    if a == b: 
    	ans+="0"
    else:
    	ans+="1"
print(ans)