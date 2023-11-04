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
    i = 1
    j = n
    cur = i
    cnt = 0
    ans = []
    while cnt < k - 1:
        if cur == i:
            ans.append(i)
            i += 1
            cur = j
        else:
            ans.append(j)
            j -= 1
            cur = i
        cnt += 1
    if cur == i:
        for num in range(i, j + 1):
            ans.append(num)
    else:
        for num in range(j, i - 1, -1):
            ans.append(num)
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
