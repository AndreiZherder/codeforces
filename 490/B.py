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
    n = int(input())
    ans = [0 for i in range(n)]
    pair1 = dict()
    pair2 = dict()
    for i in range(n):
        a, b = [int(num) for num in input().split()]
        pair1[a] = b
        pair2[b] = a
    if n % 2 == 0:
        cur = 0
        for i in range(n // 2):
            cur = pair1[cur]
            ans[i * 2 + 1] = cur
        cur = 0
        for i in range(n // 2):
            cur = pair2[cur]
            ans[n - 1 - i * 2 - 1] = cur
    else:
        cur = 0
        for i in range(n // 2):
            cur = pair1[cur]
            ans[i * 2 + 1] = cur
        for k in pair1:
            if k not in pair2:
                cur = k
                ans[0] = cur
        for i in range(1, n // 2 + 1):
            cur = pair1[cur]
            ans[i * 2] = cur
    print(*ans)



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
