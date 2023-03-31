import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    if n % 2 == 0:
        print(-1)
        return
    cnt = 0
    ans = deque()
    while n > 1:
        if (n + 1) // 2 % 2 == 1:
            cnt += 1
            ans.appendleft(1)
            n = (n + 1) // 2
        else:
            cnt += 1
            ans.appendleft(2)
            n = (n - 1) // 2
    print(cnt)
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
