def solution():
    h, m = (int(num) for num in input().split())
    # 23 55
    ans = (23 - h) * 60 + 60 - m
    print(ans)

t = int(input())

while t:
    solution()
    t -= 1