# 03:36
import copy

# 우 상 좌 하
dirs = [(1,0),(0,-1),(-1,0),(0,1)]
move_info = [(0,0,0),(0,-1,3),(-1,-1,2),(-1,0,1)]
edge_dict = {}


def move(x,y,d):
  dx, dy = dirs[d]
  nx, ny = dx+x, dy+y
  for info_x, info_y, i in move_info:
    key = f'{info_x+nx},{info_y+ny}'
    if key not in edge_dict:
      edge_dict[key] = [False]*4
    edge_dict[key][i] = True
  return nx, ny

def make_path(d):
  path = [d]
  for _ in range(1, g+1):
    path += [(i+1)%4 for i in reversed(copy.deepcopy(path))]
  return path

n = int(input())
infos = []
for _ in range(n):
  infos.append(list(map(int, input().split())))
  
for x,y,d,g in infos:
  cx,cy = x,y
  for info_x, info_y, i in move_info:
    key = f'{info_x+x},{info_y+y}'
    if key not in edge_dict:
      edge_dict[key] = [False]*4
    edge_dict[key][i] = True
  for cd in make_path(d):
    cx,cy = move(cx,cy,cd)

print(sum([1 for val in edge_dict.values() if all(val)]))