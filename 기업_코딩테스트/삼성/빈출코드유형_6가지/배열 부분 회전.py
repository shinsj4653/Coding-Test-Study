# https://velog.io/@rhdmstj17/%EC%82%BC%EC%84%B1-%EC%9D%B8%EC%9E%AC%EC%9B%90-%EB%93%A4%EC%96%B4%EA%B0%80%EA%B8%B0-%EC%A0%84-%EC%88%99%EC%A7%80%ED%95%98%EA%B3%A0-%EB%93%A4%EC%96%B4%EA%B0%80%EB%A9%B4-%EC%A2%8B%EC%9D%80-%EB%B9%88%EC%B6%9C-%EC%BD%94%EB%93%9C-%EC%9C%A0%ED%98%95-6%EA%B0%80%EC%A7%80

def rotated_90(a):
  m= len(a) # 3 원래 세로 -> 이젠 가로
  n = len(a[0]) # 4 원래 가로 -> 이젠 세로
  result = [[0] * m for _ in range(n)] # 배열의 가로 세로 길이가 뒤바뀌는 것 주의
  for i in range(m): # 범위 주의
    for j in range(n): # 범위 주의
      result[j][m - i - 1] = a[i][j]
  return result

# 0, 0 -> 0, 2
# 0, 1 -> 1, 2
# 0, 2 -> 2, 2
# 0, 3 -> 3, 2

a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

# 9 5 1
# 10 6 2
# 11 7 3
# 12 8 4

print(rotated_90(a))