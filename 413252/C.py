def solution():
    n = int(input())
    if n == 0:
        print(0)
        return
    if (n + 1) % 2 == 0:
        print((n + 1) // 2)
    else:
        print(n + 1)


t = 1
while t:
    solution()
    t -= 1