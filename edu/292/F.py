from collections import deque
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
    n, k = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    j = 0
    ans = 0
    maxq = deque()
    minq = deque()
    for i in range(n):
        while maxq and nums[maxq[-1]] <= nums[i]:
            maxq.pop()
        maxq.append(i)
        while minq and nums[minq[-1]] >= nums[i]:
            minq.pop()
        minq.append(i)
        while maxq and minq and nums[maxq[0]] - nums[minq[0]] > k:
            j += 1
            while maxq and maxq[0] < j:
                maxq.popleft()
            while minq and minq[0] < j:
                minq.popleft()
        ans += i - j + 1
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
