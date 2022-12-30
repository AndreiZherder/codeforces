from collections import deque


def solution():
    n, k = (int(num) for num in input().split())
    if n == 1:
        print(1)
        return
    q = deque(range(1, n + 1))
    for i in range(n):
        if i % 2 == 0:
            print(q.pop(), end=' ')
        else:
            print(q.popleft(), end=' ')
    print()


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
