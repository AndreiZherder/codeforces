def solution():
    n, k = (int(num) for num in input().split())
    nums = [int(num) for num in input().split()]
    j = 1
    cnt = 0
    for num in nums:
        if num == j:
            cnt += 1
            j += 1
    print((n - cnt + k - 1) // k)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
