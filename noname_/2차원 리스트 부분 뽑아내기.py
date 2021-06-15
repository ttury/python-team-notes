field = [
  [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
  [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)],
  [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
  [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
  [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)], 
]

# 직사각형의 두 좌표를 이용해 특정 부분을 빼냄
def GetSectionByLocation(field, lefttop, rightbottom):
  y1, x1 = lefttop
  y2, x2 = rightbottom
  result = [row[x1:x2+1] for row in field[y1:y2+1]]
  return result

# 전체 행렬에서 지정한 차원(m x n)의 가능한 모든 부분행렬을 빼냄
def GetSectionByShape(field, m_sect, n_sect):
  m_field = len(field)
  n_field = len(field[0])
  result = []
  for i in range(m_field - m_sect + 1):
    for j in range(n_field - n_sect + 1):
      result.append([row[j:j+n_sect] for row in field[i:i+m_sect]])

  return result

def printMatrix(matrix):
  for row in matrix:
    print(row)

# 테스트
print("original field(5 x 5)")
printMatrix(field)
print()

section = GetSectionByLocation(field, (1, 1), (3, 3))
print("segment by location((1,1) ~ (3,3))")
printMatrix(section)
print()

print("every segment by shape(3 x 2)")
sections = GetSectionByShape(field, 3, 2)
for section in sections:
  printMatrix(section)
  print("-----------")