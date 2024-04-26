from os import path
from sys import stdin, stdout


filename = '../../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    ans = []
    i = 0
    j = 0
    cnt = 0
    while i < n and j < m:
        if a[i] < b[j]:
            i += 1
            cnt += 1
        else:
            ans.append(cnt)
            j += 1
    if i == n:
        ans.extend([cnt] * (m - j))
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
