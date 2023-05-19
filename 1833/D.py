import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    if n == 1:
        print(1)
        return
    maxi = a.index(n)
    if maxi == 0:
        maxi = a.index(n - 1)
    if maxi == 1:
        print(*(a[maxi:] + [a[0]]))
        return
    i = maxi - 2
    while i > 0 and a[i] > a[0]:
        i -= 1
    i += 1
    perm1 = a[maxi:] + a[i:maxi][::-1] + a[:i]
    if maxi != n - 1:
        print(*perm1)
        return
    else:
        perm2 = [a[maxi]] + a[:maxi]
        perm3 = [a[maxi]] + a[:maxi][::-1]
        ans = max(perm1, perm2, perm3)
        print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
