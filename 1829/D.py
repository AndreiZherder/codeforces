import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def dfs(n: int, m: int) -> bool:
        if n == m:
            return True
        if n % 3 != 0:
            return False
        return dfs(n // 3, m) or dfs(2 * n // 3, m)

    n, m = [int(num) for num in input().split()]
    if dfs(n, m):
        print('YES')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
