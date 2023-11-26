# 03:00
n,l = map(int, input().split())
roads = []
for _ in range(n):
  roads.append(list(map(int, input().split())))

answer = 0

def find_road(is_row):
  global answer
  for a in range(n):
    can_pass = True
    temp_height = roads[a][0] if is_row else roads[0][a]
    temp_count = 0
    # 내려가면 True
    is_down = False
    for b in range(n):
      # print(f'x:{x}, y:{y}, temp_height:{temp_height}, temp_count:{temp_count}, is_down:{is_down}')
      current_height = roads[a][b] if is_row else roads[b][a]
      # 현재 높이와 이전 높이가 같으면 통과
      if temp_height == current_height:
        temp_count += 1
        continue
      
      # 높이차 구하기
      height_diff = temp_height - current_height
      # 현재 높이와 이전 높이의 차이가 1보다 크면 break
      if abs(height_diff) > 1:
        can_pass = False
        break
      # 현재 높이로 올 때 내리막인가?
      current_is_down = height_diff > 0
      # 경사로를 놓는데 필요한 칸 수
      temp = 0
      temp += (l if is_down else 0)
      temp += (l if not current_is_down else 0)

      # 경사로를 놓을 수 없으면 break
      if temp_count < temp:
        can_pass = False
        break
      # 초기화
      temp_count = 1
      temp_height = current_height
      is_down = current_is_down
    if can_pass and (not is_down or temp_count >= l):
      answer += 1

find_road(True)
find_road(False)
print(answer)