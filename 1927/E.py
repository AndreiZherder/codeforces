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
    p = [0 for i in range(n)]
    low = 1
    high = n
    q = k // 2
    left = 0
    right = k - 1
    while q:
        if q % 2 == 0:
            p[left] = high
            p[right] = low
            i = left + k
            while i < n:
                p[i] = p[i - k] - 1
                i += k
                high -= 1
            i = right + k
            while i < n:
                p[i] = p[i - k] + 1
                i += k
                low += 1
        else:
            p[left] = low
            p[right] = high
            i = left + k
            while i < n:
                p[i] = p[i - k] + 1
                i += k
                low += 1
            i = right + k
            while i < n:
                p[i] = p[i - k] - 1
                i += k
                high -= 1
        left += 1
        right -= 1
        high -= 1
        low += 1
        q -= 1
    print(*p)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
