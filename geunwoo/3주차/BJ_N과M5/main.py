n: int
m: int
sqnc: list
answer = []
visited = []


def backtracking(level: int):
    global n, m, sqnc, answer, visited
    if level == m:
        print(*answer)
        return

    for i in range(n):
        if visited[i] == 1:
            continue

        visited[i] = 1
        answer.append(sqnc[i])

        backtracking(level+1)

        answer.pop()
        visited[i] = 0


def main():
    global n, m, sqnc, answer, visited

    n, m = map(int, input().split())
    sqnc = list(map(int, input().split()))
    sqnc.sort()
    visited = [0] * (n + 1)

    backtracking(0)


if __name__ == "__main__":
    main()
