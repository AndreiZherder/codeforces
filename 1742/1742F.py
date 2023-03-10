import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    q = int(input())
    mxt = 'a'
    mns = 'a'
    lt = 1
    ls = 1
    sets = {'a'}
    sett = {'a'}
    while q:
        m, k, x = input().split()
        k = int(k)
        if m == '1':
            mns = min(mns, min(x))
            ls += k * len(x)
            sets |= set(x)
        else:
            mxt = max(mxt, max(x))
            lt += k * len(x)
            sett |= set(x)
        if mxt > mns or (len(sets) == 1 and len(sett) == 1 and lt > ls):
            print('YES')
        else:
            print('NO')
        q -= 1


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
