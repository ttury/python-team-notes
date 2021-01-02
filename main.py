d = [0] * 100

def ant_warriors(x, n, k):
  if x > n:
    return 0
  
  d[x] =  k[x] + max(k[x + 2], k[x + 3])            

n = int(input())
k = list(map(int, input().split()))

for i in range(1, n + 1):
  if i > n:
    break
  d[x] = 