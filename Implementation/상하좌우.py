n = int(input())
travel_plans = input().split()

dx = [-1, 0, 1, 0] #U, R, D, L
dy = [0, 1, 0, -1]

x = 1
y = 1

travel_types = ['U', 'R', 'D', 'L']

for travel_plan in travel_plans:
  for i in range(len(travel_types)):
    if travel_plan == travel_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if(nx > n or nx < 1 or ny > n or ny < 1):
    continue
  x, y = nx, ny

print(x, y)