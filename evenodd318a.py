n , k = map(int , input().split())
if n%2 == 0:
  if n/2 >= k:
    print(k*2-1)
  else:
    print((k - n//2)*2)
else:
  if n/2 + 1 >= k:
    print(k*2 - 1)
  else:
    print((k - n//2 - 1)*2)