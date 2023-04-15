import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    s = input()
    n = len(s)
    s *= 2
    best = 0
    cur = 0
    for c in s:
        if c == '1':
           cur += 1
           best = max(best, cur)
        else:
            cur = 0
    if best == 0:
        print(0)
    elif best == 2 * n:
        print(n ** 2)
    elif best == 1:
        print(1)
    else:
        if best % 2 == 1:
            x = (best + 1) // 2
            print(x ** 2)
        else:
            x = best // 2
            print(x * (x + 1))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
