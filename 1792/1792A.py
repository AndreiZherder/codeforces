def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    ones = 0
    for num in nums:
        if num == 1:
            ones += 1
    ans = ones // 2
    ans += len(nums) - ans * 2
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
