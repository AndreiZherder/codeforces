from collections import defaultdict


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    if len(set(nums)) != len(nums):
        print('NO')
        return
    cnt = defaultdict(int)
    for num in nums:
        if num % 2 == 0:
            cnt[0] += 1
        else:
            cnt[1] += 1
    if cnt[0] >= 2 and cnt[1] >= 2:
        print('NO')
        return
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
