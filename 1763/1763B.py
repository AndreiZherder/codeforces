from heapq import heapify, heappop


def solution():
    n, k = (int(num) for num in input().split())
    hs = [(int(num), i) for i, num in enumerate(input().split())]
    ps = [(int(num), i) for i, num in enumerate(input().split())]
    heapify(hs)
    heapify(ps)
    dead = set()
    total = k
    while len(dead) < n:
        while hs[0][0] <= total:
            h, i = heappop(hs)
            dead.add(i)
            if len(dead) == n:
                print('YES')
                return
        while ps[0][1] in dead:
            heappop(ps)
        k -= ps[0][0]
        if k <= 0:
            print('NO')
            return
        total += k


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
