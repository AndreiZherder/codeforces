import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    x1, y1, x2, y2 = [int(num) for num in input().split()]

    corners = []
    corners.append(x1 == 1 and (y1 == 1 or y1 == m))
    corners.append(x1 == n and (y1 == 1 or y1 == m))
    corners.append(x2 == 1 and (y2 == 1 or y2 == m))
    corners.append(x2 == n and (y2 == 1 or y2 == m))

    if any(corners):
        print(2)
        return

    borders = []
    borders.append(x1 == 1)
    borders.append(x1 == n)
    borders.append(x2 == 1)
    borders.append(x2 == n)
    borders.append(y1 == 1)
    borders.append(y1 == m)
    borders.append(y2 == 1)
    borders.append(y2 == m)

    if any(borders):
        print(3)
        return

    print(4)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
