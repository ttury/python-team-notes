def sequential_search(n, array, target):
  for i in range(n):
    if array[i] == target:
      return "yes"
  
  return "no"

n = int(input())
array = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
  print(sequential_search(n, array, target), end=' ')
  print()