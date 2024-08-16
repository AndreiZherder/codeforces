from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, q = [int(num) for num in input().split()]
    a = input()
    b = input()
    prefa = [[0 for j in range(n + 1)] for i in range(26)]
    prefb = [[0 for j in range(n + 1)] for i in range(26)]
    for j in range(n):
        for i in range(26):
            if a[j] == chr(ord('a') + i):
                prefa[i][j + 1] = prefa[i][j] + 1
            else:
                prefa[i][j + 1] = prefa[i][j]
            if b[j] == chr(ord('a') + i):
                prefb[i][j + 1] = prefb[i][j] + 1
            else:
                prefb[i][j + 1] = prefb[i][j]
    while q:
        l, r = [int(num) - 1 for num in input().split()]
        ans = 0
        for i in range(26):
            ans += abs(prefb[i][r + 1] - prefb[i][l] - (prefa[i][r + 1] - prefa[i][l]))
        print(ans // 2)
        q -= 1


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
