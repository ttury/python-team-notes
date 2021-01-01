def seqauntial_search(n, target, array):
  for i in range(n):
    if array[i] == target:
      return i + 1

print("생성할 원소 개수와 찾을 문자열을 입력하세요")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("원소 개수만큼 문자열을 입력하세요.");
array = input().split()

print(seqauntial_search(n, target, array))