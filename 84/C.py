from bisect import bisect_left
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
    points = []
    for i in range(n):
        points.append([int(num) for num in input().split()] + [i])
    m = int(input())
    shots = []
    for i in range(m):
        shots.append([int(num) for num in input().split()])
    cnt = 0
    ans = [-1 for i in range(n)]
    points.sort()
    for i, (x1, y1) in enumerate(shots):
        jr = bisect_left(points, [x1, 0, 0])
        jl = jr - 1
        if jr < n:
            if ans[points[jr][2]] == -1:
                if (x1 - points[jr][0]) ** 2 + y1 ** 2 <= points[jr][1] ** 2:
                    cnt += 1
                    ans[points[jr][2]] = i + 1
        if jl >= 0:
            if ans[points[jl][2]] == -1:
                if (x1 - points[jl][0]) ** 2 + y1 ** 2 <= points[jl][1] ** 2:
                    cnt += 1
                    ans[points[jl][2]] = i + 1
    print(cnt)
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
