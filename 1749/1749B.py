from heapq import heapify, heappop


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    i = 0
    j = n - 1
    ans = 0
    while i <= j:
        if b[i] < b[j]:
            ans += a[i]
            a[i + 1] += b[i]
            i += 1
        else:
            ans += a[j]
            if j > 0:
                a[j - 1] += b[j]
            j -= 1

    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
