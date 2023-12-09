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
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    indexes = sorted(range(n), key=lambda i: b[i])
    for i in indexes:
        L = -1
        R = n
        l = i
        r = i
        if a[i] > b[i]:
            print('NO')
            return
        while l >= 0 and a[l] < b[i]:
            l -= 1
        if l >= 0:
            if a[l] == b[i]:
                L = l
        while r < n and a[r] < b[i]:
            r += 1
        if r < n:
            if a[r] == b[i]:
                R = r
        if L != -1:
            if all(b[j] >= b[i] for j in range(i, L - 1, -1)):
                continue
        if R != n:
            if all(b[j] >= b[i] for j in range(i, R + 1)):
                continue
        print('NO')
        return
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
