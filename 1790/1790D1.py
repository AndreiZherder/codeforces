from collections import Counter
from heapq import heapify, heappop, heappush


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    c = Counter(a)
    h = [(k, v) for k, v in c.items()]
    heapify(h)
    ans = 0
    stack = []
    while h:
        i, cnt = heappop(h)
        cnt -= 1
        if cnt > 0:
            stack.append((i, cnt))
        while h and h[0][0] == i + 1:
            i, cnt = heappop(h)
            cnt -= 1
            if cnt > 0:
                stack.append((i, cnt))
        ans += 1
        while stack:
            heappush(h, stack.pop())
    print(ans)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
