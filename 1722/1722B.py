


def solution():
    n = int(input())
    row1 = input()
    row2 = input()
    row1 = row1.replace('G', 'B')
    row2 = row2.replace('G', 'B')
    for c1, c2 in zip(row1, row2):
        if c1 != c2:
            print('NO')
            return
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
