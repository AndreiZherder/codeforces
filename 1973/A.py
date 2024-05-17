from heapq import heapify, heappop, heappush
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
    nums = [int(num) for num in input().split()]
    total = sum(nums)
    if total % 2 == 1:
        print(-1)
    else:
        ans = 0
        nums = [-num for num in nums if num != 0]
        heapify(nums)
        while len(nums) > 1:
            p1 = -heappop(nums)
            p2 = -heappop(nums)
            ans += 1
            if p1 > 1:
                p1 -= 1
                heappush(nums, -p1)
            if p2 > 1:
                p2 -= 1
                heappush(nums, -p2)
        print(ans)





def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
