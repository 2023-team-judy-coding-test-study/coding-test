print(int ( -1 / 3))
print(-1 // 3)

N = int(input())
nums = [ int(x) for x in input().split() ]
add, sub, mul, div = map(int, input().split()) # 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수

max_value = -int(1e9)
min_value = int(1e9)

def dfs(curr, data):
    global add, sub, mul, div, max_value, min_value

    if curr == N:
        max_value = max(max_value, data)
        min_value = min(min_value, data)
        return
    
    if add > 0:
        add -= 1
        dfs(curr + 1, data + nums[curr])
        add += 1
    
    if sub > 0:
        sub -= 1
        dfs(curr + 1, data - nums[curr])
        sub += 1

    if mul > 0:
        mul -= 1
        dfs(curr + 1, data * nums[curr])
        mul += 1

    if div > 0:
        div -= 1
        dfs(curr + 1, int(data / nums[curr]))
        div += 1
    
dfs(1, nums[0])
print(max_value)
print(min_value)