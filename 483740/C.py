def solution():
    h, l = [int(num) for num in input().split()]
    print((l ** 2 - h ** 2) / (2 * h))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
