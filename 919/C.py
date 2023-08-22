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
    n, m, k = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append(input())
    ans = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            if a[i][j] == '.':
                cur += 1
            else:
                if cur >= k:
                    ans += cur - k + 1
                cur = 0
        if cur >= k:
            ans += cur - k + 1

    if k == 1:
        print(ans)
        return

    for j in range(m):
        cur = 0
        for i in range(n):
            if a[i][j] == '.':
                cur += 1
            else:
                if cur >= k:
                    ans += cur - k + 1
                cur = 0
        if cur >= k:
            ans += cur - k + 1

    print(ans)




def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
