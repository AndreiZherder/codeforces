def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    nums = sorted(a[1:])
    n = len(nums)
    total = a[0]
    i = 0
    while i < n:
        if nums[i] > total:
            total += (nums[i] + 1 - total) // 2
        i += 1
    print(total)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
