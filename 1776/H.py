import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = {int(num): i for i, num in enumerate(input().split())}
    b = [int(num) for num in input().split()]
    ans = 0
    for i in range(n - 1, 0, -1):
        if a[b[i - 1]] > a[b[i]]:
            ans = i
            break
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
