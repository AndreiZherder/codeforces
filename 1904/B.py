from bisect import bisect_right
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
    nums = sorted([(int(num), i) for i, num in enumerate(input().split())])
    pref = [nums[0][0]]
    for i in range(1, n):
        pref.append(pref[-1] + nums[i][0])
    stops = []
    for i in range(1, n):
        if nums[i][0] > pref[i - 1]:
            stops.append(i)
    ans = [0 for i in range(n)]
    for i in range(n):
        index = nums[i][1]
        cnt = i
        j = bisect_right(stops, i)
        if j == len(stops):
            j = n
        else:
            j = stops[j]
        cnt += j - i - 1
        ans[index] = cnt
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
