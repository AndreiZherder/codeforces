def solution():
    # 0 1 2 3 4
    # pos = (start + move) % n
    # (0 + 6) % 5 = 1
    # (0 - 1) % 5 = 4
    # (0 - 1) % 5 = -1
    # n + (0 - 1) % 5 = 4
    n, a, b = (int(num) for num in input().split())
    ans = (a - 1 + b) % n + 1
    print(ans)


t = 1
while t:
    solution()
    t -= 1