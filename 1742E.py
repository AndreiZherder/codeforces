from bisect import bisect_right
from itertools import accumulate


def solution():
    n, q = map(int, input().split())
    a = [int(num) for num in input().split()]
    k = [int(num) for num in input().split()]
    ans = []
    acc = list(accumulate(a, initial=0))
    b = []
    maximum = -float('Inf')
    for num in a:
        maximum = max(maximum, num)
        b.append(maximum)
    for j in range(q):
        index = bisect_right(b, k[j])
        if index == len(b):
            ans.append(acc[-1])
        else:
            ans.append(acc[index])
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
