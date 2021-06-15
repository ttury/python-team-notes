d = [0] * 101 # d[99] -> f(0) 부터 f(99)까지 거쳐온 노드 비용 최댓값

n = int(input()) # 3 ~ 100크기
k = list(map(int, input().split())) # 각 0 ~ 1000크기

d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
  d[i] = max(d[i - 1], (d[i - 2] + k[i]))

print(d[n - 1])