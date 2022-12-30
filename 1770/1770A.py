from heapq import heapify, heappop, heappush


def solution():
    n, m = (int(num) for num in input().split())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    heapify(a)
    for num in b:
        heappop(a)
        heappush(a, num)
    print(sum(a))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
