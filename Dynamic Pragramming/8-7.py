d = [0] * 1001 # d[k] = 1열부터 k열까지 경우의 수

n = int(input())

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
  d[i] = d[i - 1] + 2 * d[i - 2]

print(d[n])