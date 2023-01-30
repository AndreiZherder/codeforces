from collections import Counter
from sortedcontainers import SortedDict


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    c = SortedDict(Counter(a))
    ans = 0
    while c:
        i = c.peekitem(0)[0]
        c[i] -= 1
        if c[i] == 0:
            del c[i]
        while i + 1 in c:
            i += 1
            c[i] -= 1
            if c[i] == 0:
                del c[i]
        ans += 1
    print(ans)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
