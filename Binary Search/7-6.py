n = int(input())
array = [0] * 1000000

for i in input().split():
  array[int(i)] += 1

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
  if array[target]:
    print('yes', end=' ')
  else:
    print('no', end=' ')