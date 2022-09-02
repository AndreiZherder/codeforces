
def solution():
    n = int(input())
    print(n // 3 * 5 + (n // 2 - n // 3) * 3 + n - n // 2)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
