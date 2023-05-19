import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    a = [(int(num), i) for i, num in enumerate(input().split())]
    b = [(int(num), i) for i, num in enumerate(input().split())]
    a.sort()
    b.sort()
    ans = [0 for i in range(n)]
    for (numa, i), (numb, j) in zip(a, b):
        ans[i] = numb
    print(*ans)




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
