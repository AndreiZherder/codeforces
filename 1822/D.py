import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    if n == 1:
        print(1)
        return
    if n % 2 == 1:
        print(-1)
        return
    a = [n]
    cur = 1
    for i in range(n - 1):
        if i % 2 == 0:
            a.append((n - cur))
        else:
            a.append(cur)
        cur += 1
    print(*a)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
