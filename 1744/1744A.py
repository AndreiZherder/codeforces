

def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    s = input()
    d1 = dict()
    for num, c in zip(a, s):
        if num in d1:
            if d1[num] != c:
                print('NO')
                return
        else:
            d1[num] = c
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
