from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    r = int(input())
    if r <= 1399:
        print('Division 4')
    elif r <= 1599:
        print('Division 3')
    elif r <= 1899:
        print('Division 2')
    else:
        print('Division 1')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
