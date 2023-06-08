import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    mod = 1000000007
    fact = [0 for i in range(n + 1)]
    fact[1] = 1
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % mod
    p = 0
    add = 0
    for i in range(2, n + 1):
        add += 2
        p = (p + add) % mod
    ans = (fact[n] * p) % mod
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
