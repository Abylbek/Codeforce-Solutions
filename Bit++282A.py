n = int(input())
tot = 0
for i in range(n):
    k = input()
    if k[0] == '+' or k[1] == '+':
        tot+=1
    else:
        tot-=1
print(tot)
