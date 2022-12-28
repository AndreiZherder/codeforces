def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    ans = 1
    for num in nums:
        if num != 1:
            ans *= num
    print(2022 * (ans + n - 1))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
