def solution():
    n, w, h = (int(num) for num in input().split())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    mx = -10 ** 20
    mn = 10 ** 20
    for x, y in zip(a, b):
        mx = max(mx, y + h - x - w)
        mn = min(mn, y - h - x + w)
    if mx <= mn:
        print('YES')
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
