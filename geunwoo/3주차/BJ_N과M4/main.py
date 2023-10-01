n: int
m: int
visited = []
answer = []


def backtracking(idx: int, level: int):
    global n, m, answer, visited
    # 종료 조건
    if level == m:
        if sorted(answer) in visited:
            print(answer)
            print(visited)
            return

        print(*answer)
        visited.append(sorted(answer))
        return

    # 가지 치기
    for i in range(idx, n+1):
        answer.append(i)
        backtracking(i, level+1)
        answer.pop()


def main():
    global n, m
    n, m = map(int, input().split())

    backtracking(1, 0)


if __name__ == "__main__":
    main()
