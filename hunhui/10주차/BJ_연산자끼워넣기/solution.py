# 02:53
n = map(int, input().split())
nums = list(map(int, input().split()))
operator_counts = list(map(int, input().split()))
max_count = len(nums) - 1
max_answer = -1000000000
min_answer = 1000000000
def backtracking(count, answer, s):
  global min_answer, max_answer
  if count == max_count:
    min_answer = min(min_answer, answer)
    max_answer = max(max_answer, answer)
    return
  for i, oc in enumerate(operator_counts):
    if oc <= 0:
      continue
    operator_counts[i] -= 1
    if i == 0:
      backtracking(count + 1, answer + nums[count+1], s+'+'+str(nums[count+1]))
    elif i == 1:
      backtracking(count + 1, answer - nums[count+1], s+'-'+str(nums[count+1]))
    elif i == 2:
      backtracking(count + 1, answer * nums[count+1], s+'*'+str(nums[count+1]))
    elif i == 3:
      new_answer = answer // nums[count+1] if answer >= 0 else (-1 * answer) // nums[count+1] * (-1)
      backtracking(count + 1, new_answer, s+'/'+str(nums[count+1]))
    operator_counts[i] += 1
backtracking(0, nums[0], str(nums[0]))
print(max_answer)
print(min_answer)