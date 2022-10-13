

def solution():
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[2] == nums[0] + nums[1]:
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
