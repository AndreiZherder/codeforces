def solution():
    s = input()
    print(s + s[::-1])


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
