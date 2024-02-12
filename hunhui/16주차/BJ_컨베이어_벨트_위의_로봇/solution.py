def simulate_conveyor_belt(N, K, A):
    # 컨베이어 벨트의 내구도
    belt_durability = A[:]
    # 벨트 위의 로봇 위치 (True: 로봇 있음, False: 로봇 없음)
    robots_on_belt = [False] * (2 * N)
    step = 0

    while True:
        step += 1
        # 1. 벨트 회전
        last_durability = belt_durability.pop()
        belt_durability.insert(0, last_durability)
        last_robot = robots_on_belt.pop()
        robots_on_belt.insert(0, last_robot)
        
        # 내리는 위치에 로봇이 있다면 내림
        robots_on_belt[N-1] = False

        # 2. 로봇 이동
        for i in range(N-2, -1, -1):
            if robots_on_belt[i] and not robots_on_belt[i+1] and belt_durability[i+1] > 0:
                robots_on_belt[i] = False
                robots_on_belt[i+1] = True
                belt_durability[i+1] -= 1
        # 내리는 위치에 로봇이 있다면 내림
        robots_on_belt[N-1] = False

        # 3. 새 로봇 올리기
        if belt_durability[0] > 0:
            robots_on_belt[0] = True
            belt_durability[0] -= 1

        # 4. 내구도가 0인 칸의 개수 확인
        if belt_durability.count(0) >= K:
            break

    return step

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(simulate_conveyor_belt(n, k, a))