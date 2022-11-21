def solution():
    n = int(input())
    s = input()
    print(ord(max(s)) - ord('a') + 1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
