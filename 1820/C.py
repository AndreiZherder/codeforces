import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def find_mex(s) -> str:
        for i in range(200001):
            if str(i) not in s:
                return str(i)

    n = int(input())
    a = [num for num in input().split()]
    s = set(a)
    mex = find_mex(s)
    if str(int(mex) + 1) not in s:
        if int(mex) > max(int(num) for num in s):
            if len(a) == len(s):
                print('NO')
                return
            else:
                print('YES')
                return
        else:
            print('YES')
            return

    left = a.index(str(int(mex) + 1))
    right = n - a[::-1].index(str(int(mex) + 1)) - 1
    a[left: right + 1] = [mex] * (right - left + 1)

    s = set(a)
    if find_mex(s) == str(int(mex) + 1):
        print('YES')
        return
    else:
        print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
