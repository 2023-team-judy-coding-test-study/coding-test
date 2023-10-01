n: int
m: int
answer = []


def back(start, level):
    global n, m, answer

    # 종료 조건
    if level == m:
        print(*answer)
        return

    for i in range(start, n+1):
        answer.append(i)
        back(i + 1, level + 1)
        answer.pop()


def main():
    global n, m, answer
    n, m = map(int, input().split())

    back(1, 0)


if __name__ == "__main__":
    main()
