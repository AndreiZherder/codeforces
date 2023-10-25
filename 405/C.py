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
    a = []
    for i in range(n):
        a.append([int(num) % 2 for num in input().split()])
    product = 0
    for i in range(n):
        cur = 0
        for j in range(n):
            cur += a[i][j] * a[j][i]
        product += cur
        product %= 2
    q = int(input())
    ans = []
    while q:
        command = input().split()
        if len(command) == 2:
            product ^= 1
        else:
            ans.append(str(product))
        q -= 1
    print(''.join(ans))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
