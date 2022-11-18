def solution():
    l, r, x = (int(num) for num in input().split())
    a, b = (int(num) for num in input().split())
    if a == b:
        print(0)
        return
    if r - a < x and a - l < x:
        print(-1)
        return
    if r - b < x and b - l < x:
        print(-1)
        return
    if abs(b - a) >= x:
        print(1)
        return
    if b < a:
        a, b = b, a
    if a - l >= x:
        print(2)
        return
    if r - b >= x:
        print(2)
        return
    print(3)
    return


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
