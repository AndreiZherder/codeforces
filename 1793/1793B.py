import sys
from collections import deque

input = sys.stdin.readline


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    x, y = (int(num) for num in input().split())
    a = max(x, y)
    b = min(x, y)
    n = (a - b) * 2
    ans = deque([a])
    j = a - 1
    for i in range(n // 2):
        ans.append(j)
        j -= 1
    j = a - 1
    for i in range(n // 2 - 1):
        ans.appendleft(j)
        j -= 1
    print(n)
    print(*ans)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
