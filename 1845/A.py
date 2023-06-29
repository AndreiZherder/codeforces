from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k, x = [int(num) for num in input().split()]
    if x != 1:
        print('YES')
        print(n)
        print(*([1] * n))
    else:
        if n == 1:
            print('NO')
            return
        if n % 2 == 0:
            if k < 2:
                print('NO')
                return
            print('YES')
            print(n // 2)
            print(*([2] * (n // 2)))
        else:
            if k < 3:
                print('NO')
                return
            print('YES')
            print(1 + (n - 3) // 2)
            print(*([3] + [2] * ((n - 3) // 2)))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
