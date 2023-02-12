import sys
input = sys.stdin.readline


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    l = 0
    r = n - 1
    mx = n
    mn = 1
    while r - l >= 3:
        if a[l] == mn:
            l += 1
            mn += 1
        elif a[l] == mx:
            l += 1
            mx -= 1
        elif a[r] == mn:
            r -= 1
            mn += 1
        elif a[r] == mx:
            r -= 1
            mx -= 1
        else:
            print(l + 1, r + 1)
            return
    print(-1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
