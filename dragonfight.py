import math
n = int(input())
for i in range(n):
    a , b , c = map(int , input().split())
    for i in range(b):
        if math.floor((a/2)+10) <= a:
            break  
        a = math.floor(a/2)+10          
    a = a - 10*c
    print(a)
    if a <= 0:
        print("YES")
    else:
        print("NO")