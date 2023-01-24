def solution():
    nums = [int(num) for num in input().split()]
    if all(num == 0 for num in nums):
        print(0)
        return
    if nums[0] == 0:
        print(1)
        return
    a = nums[0]
    b = min(nums[1], nums[2]) * 2
    c = max(nums[1], nums[2]) - min(nums[1], nums[2])
    d = min(nums[0] + 1, c + nums[3])
    print(a + b + d)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
