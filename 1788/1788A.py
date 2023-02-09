import sys
from collections import Counter

input = sys.stdin.readline
print_list = lambda arr: sys.stdout.write(" ".join(map(str, arr)) + "\n")



def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    c = Counter(a)
    if c[1] == n:
        print(1)
        return
    x = c[2]
    if x % 2 == 1:
        print(-1)
        return
    else:
        x //= 2
        cnt = 0
        i = 0
        while cnt < x:
            if a[i] == 2:
                cnt += 1
            i += 1
        print(i)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
