from heapq import heapify, heappop


def solution():
    n, c = (int(num) for num in input().split())
    a = [int(num) + i + 1 for i, num in enumerate(input().split())]
    heapify(a)
    total = 0
    ans = 0
    while a:
        cur = heappop(a)
        if cur + total <= c:
            ans += 1
            total += cur
        else:
            break
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
