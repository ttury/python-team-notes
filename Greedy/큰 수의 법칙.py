import time

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort(reverse = True)
result = 0
j = 0

start_time = time.time()

for _ in range(m):
  if(j >= k):
    result += array[1]
    j = 0
    continue
  result += array[0]
  j += 1

end_time = time.time()

print(result)
print(f'소요 시간:{end_time - start_time}')