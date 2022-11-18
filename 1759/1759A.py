def solution():
    s = input()
    t = 'Yes' * 20
    if s in t:
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
