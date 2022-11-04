def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    print(abs(sum(a)))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
