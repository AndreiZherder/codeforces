import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]

    positive = []
    negative = []
    for num in a:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    ans = -10 ** 20
    positive.sort()
    negative.sort()
    if len(positive) >= 2:
        ans = max(ans, positive[-1] * positive[-2])
    if len(negative) >= 2:
        ans = max(ans, negative[0] * negative[1])
    if len(positive) == 1 and len(negative) == 1:
        ans = max(ans, negative[0] * positive[0])
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
