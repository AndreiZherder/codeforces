def solution():
    xs = [int(num) for num in input().split()]
    print(max(xs) - min(xs))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
