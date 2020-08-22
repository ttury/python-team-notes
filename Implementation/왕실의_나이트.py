pos_origin = input()

y_types = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

steps = [(-2, -1), (-2, 1), (1, 2), (1, -2), (2, -1), (2, 1), (-1, -2), (-1, 2)]

y = pos_origin[0]
x = int(pos_origin[1])

#알파벳인 y좌표를 정수로 변환
for i in range(len(y_types)):
  if y == y_types[i]:
    y = i + 1
    continue

count = 0

for i in range(8):
  nx = x + int(steps[i][0])
  ny = y + int(steps[i][1])
  if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
    count += 1

print(count)