from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    total = 0
    m = 0
    for num in a:
        total += num
        if num < 0:
            m += 1
    if total >= 0:
        if m % 2 == 0:
            print(0)
            return
        else:
            print(1)
            return
    else:
        total = abs(total)
        x = (total + 1) // 2
        if (x % 2 == 0 and m % 2 == 1) or (x % 2 == 1 and m % 2 == 0):
            x += 1
        print(x)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
