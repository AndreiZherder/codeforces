import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    i = a.index(1) + 1
    j = a.index(2) + 1
    k = a.index(n) + 1
    if j < i:
        i, j = j, i
    if i < k < j:
        print(k, k)
    elif k < i:
        print(k, i)
    else:
        print(j, k)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
