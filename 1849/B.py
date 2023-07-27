from heapq import heapify, heappop
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def ceil(x: int, y: int) -> int:
    return (x + y - 1) // y


def solution():
    n, k = [int(num) for num in input().split()]
    nums = [[int(num) % k, i] for i, num in enumerate(input().split())]
    nums1 = []
    ans = []
    for x, i in nums:
        if x == 0:
            ans.append(i + 1)
        else:
            nums1.append([x, i])
    for num, i in sorted(nums1, key=lambda x: (-x[0], x[1])):
        ans.append(i + 1)
    print(*ans)




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
