from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, q = [int(num) for num in input().split()]
    servers = [0 for i in range(n)]
    while q:
        t, k, d = [int(num) for num in input().split()]
        stack = []
        for i, time in enumerate(servers):
            if time <= t:
                stack.append(i)
                if len(stack) == k:
                    break
        if len(stack) == k:
            ans = 0
            for i in range(k):
                servers[stack[i]] = t + d
                ans += stack[i] + 1
            print(ans)
        else:
            print(-1)
        q -= 1


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
