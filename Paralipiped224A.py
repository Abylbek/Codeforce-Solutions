import math
a , b , c = map(int , input().split())
print(int(math.sqrt(a*b/c) + math.sqrt(a*c/b) + math.sqrt(b*c/a))*4)