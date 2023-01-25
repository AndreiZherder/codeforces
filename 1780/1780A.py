from collections import Counter


def solution():
    n = int(input())
    nums = [int(num) for num in input().split()]
    c = Counter()
    evens = []
    odds = []
    for i, num in enumerate(nums):
        if num % 2 == 0:
            c[0] += 1
            evens.append(i + 1)
        else:
            c[1] += 1
            odds.append(i + 1)
    if c[1] >= 3:
        print('YES')
        print(*odds[:3])
        return
    if c[1] >= 1 and c[0] >= 2:
        print('YES')
        print(odds[0], evens[0], evens[1])
        return
    else:
        print('NO')



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
