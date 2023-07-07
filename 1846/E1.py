from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    s = int(input())
    n = 3
    k = 2
    while k ** n <= s * k - s + 1:
        x = k ** n
        while x <= s * k - s + 1:
            if x == s * k - s + 1:
                print('YES')
                return
            n += 1
            x = k ** n
        k += 1
        n = 3
    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
