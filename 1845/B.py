from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    xa, ya = [int(num) for num in input().split()]
    xb, yb = [int(num) for num in input().split()]
    xc, yc = [int(num) for num in input().split()]
    dx1 = xb - xa
    dx2 = xc - xa
    dy1 = yb - ya
    dy2 = yc - ya
    ans1 = 0
    ans2 = 0
    f1 = dx1 * dx2 >= 0
    f2 = dy1 * dy2 >= 0

    if f1 and f2:
        ans1 = min(abs(dx1), abs(dx2))
        ans2 = min(abs(dy1), abs(dy2))
        print(ans1 + ans2 + 1)
        return
    elif f1:
        ans1 = min(abs(dx1), abs(dx2))
        print(ans1 + 1)
    elif f2:
        ans2 = min(abs(dy1), abs(dy2))
        print(ans2 + 1)
    else:
        print(1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
