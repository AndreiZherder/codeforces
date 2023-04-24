import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, t = [int(num) for num in input().split()]
    a = [(int(num) + i, i) for i, num in enumerate(input().split())]
    b = [int(num) for num in input().split()]
    best = 0
    besti = 0
    for num, i in a:
        if num <= t:
            if b[i] > best:
                best = b[i]
                besti = i
    if best == 0:
        print(-1)
    else:
        print(besti + 1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
