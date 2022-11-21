def solution():
    nums = [int(num) for num in input().split()]
    print(sum(nums) - max(nums) - min(nums))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
