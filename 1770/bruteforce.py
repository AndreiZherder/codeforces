from math import gcd
from random import randrange


def solution():
    n = 20
    nums = set()
    for i in range(n):
        nums.add(randrange(0, n, 2))
    # nums = [2, 4, 6, 8, 10, 12]
    nums = [1, 3, 5, 7, 9, 11]
    n = len(nums)
    cnt = 0
    for x in range(1, 1001):
        save = cnt
        for i in range(n):
            save = cnt
            for j in range(i + 1, n):
                if gcd(nums[i] + x, nums[j] + x) != 1:
                    if x % 2 == 1:
                        print(x, gcd(nums[i] + x, nums[j] + x),  i, j)
                        print([num + x for num in nums])
                    cnt += 1
                    break
            if save != cnt:
                break
        if save == cnt:
            print('x = ', x)
            break
    print(nums)
    if cnt == 1000:
        print('NO')
    else:
        print('YES')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
