from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    s = 'W' + input() + 'W'
    r = 0
    b = 0
    for i in range(n + 2):
        if s[i] == 'W':
            if i > 0 and s[i - 1] != 'W' and (r == 0 or b == 0):
                print('NO')
                return
            r = 0
            b = 0
        if s[i] == 'R':
            r += 1
        if s[i] == 'B':
            b += 1
    print('YES')



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
