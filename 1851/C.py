from collections import Counter
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    first = nums[0]
    last = nums[-1]
    if first == last:
        if nums.count(first) >= k:
            print('YES')
            return
        else:
            print('NO')
            return
    cnt = 0
    k_first_pos = -1
    for i, num in enumerate(nums):
        if num == first:
            cnt += 1
            if cnt == k:
                k_first_pos = i
    if k_first_pos == -1:
        print('NO')
        return
    cnt = 0
    for i in range(k_first_pos + 1, n):
        if nums[i] == last:
            cnt += 1
    if cnt >= k:
        print('YES')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
