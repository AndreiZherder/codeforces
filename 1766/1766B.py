def solution():
    n = int(input())
    s = input()
    if n <= 3:
        print('NO')
        return
    d = {s[0:2]}
    for i in range(2, n - 1):
        if s[i:i + 2] in d:
            print('YES')
            return
        d.add(s[i - 1:i + 1])
    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
