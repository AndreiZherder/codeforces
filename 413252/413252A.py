def solution():
    h, m = (int(num) for num in input().split())
    print((24 - h - 1) * 60 + 60 - m)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
