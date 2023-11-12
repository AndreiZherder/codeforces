from collections import deque
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
    n, k = [int(num) for num in input().split()]
    m = n // 2
    if n == 1:
        if k == 0:
            print(1)
            return
        else:
            print(-1)
            return
    if k - (m - 1) <= 0:
        print(-1)
        return
    num = 10 ** 9
    ans = []
    for i in range(m - 1):
        ans.append(num)
        num -= 1
        ans.append(num)
        num -= 1
    ans.append(k - (m - 1))
    ans.append((k - (m - 1)) * 2)
    if n % 2 == 1:
        ans.append(num)
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
