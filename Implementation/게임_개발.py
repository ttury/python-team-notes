def dfs(game_map, visited, start):
  x, y, d = start
  visited[x][y] = True
  #리스트 인덱스가 음수일때 가능한가?
  for _ in range(4):
    d -= 1
    if (d < 0):
      d = 3
    nx = x + dx[d]
    ny = y + dy[d]
    print(nx, ny)
    if not visited[nx][ny] and not game_map[nx][ny]:
      print("0발견")
      x, y = nx, ny
      start = [x, y, d]
      dfs(game_map, visited, start)
      return True
  temp = d
  d -= 2
  if d == -1:
    d = 3
  elif d == -2:
    d = 2
  nx = x + dx[d]
  ny = y + dy[d]
  print(nx, ny)
  if not game_map[nx][ny]:
      x, y = nx, ny
      start = [x, y, temp]
      dfs(game_map, visited, start)
  print('종료')
  return True

n, m = map(int, input().split())
x, y, d = map(int, input().split())
start = [x + 1, y + 1, d]
# 1부터 시작

game_map = []
game_map.append(list(map(int, [1] * (m + 2))))
for i in range(n):
  game_map.append(list(map(int, [1] + input().split() + [1])))
game_map.append(list(map(int, [1] * (m + 2))))
for i in range(n + 2):
  print(game_map[i])

# N, E, S, W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# n x m 헹렬 선언
visited = [[False] * (m + 2) for _ in range(n + 2)]

dfs(game_map, visited, start)

result = 0
for i in range(n + 2):
  for count in visited[i]:
    if count:
      result += 1
print(result)