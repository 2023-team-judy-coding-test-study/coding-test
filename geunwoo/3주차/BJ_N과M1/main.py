n: int
m: int
answer = []
visited = []


def backtracking(level: int):
    global n, m, answer, visited
    # 종료 시점
    if level == m:
        print(*answer)
        return

    # 가지치기
    for i in range(1, n + 1):
        if visited[i] == 1:
            continue
        answer.append(i)
        visited[i] = 1
        backtracking(level + 1)
        answer.pop()
        visited[i] = 0


def main():
    global n, m, answer, visited

    n, m = map(int, input().split())
    visited = [0] * (n + 1)

    backtracking(0)


if __name__ == "__main__":
    main()
