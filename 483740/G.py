def solution():
    n, k = [int(num) for num in input().split()]
    nums = [int(num) for num in input().split()]
    cur = sum(nums[:k])
    best = cur
    j = 0
    for i in range(k, n):
        cur += nums[i] - nums[i - k]
        if cur < best:
            best = cur
            j = i - k + 1
    print(j + 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
