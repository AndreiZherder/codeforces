from collections import Counter, defaultdict
from os import path
from sys import stdin, stdout
from types import GeneratorType

filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


def solution():
    @bootstrap
    def dp(i: int, rem: int, all_prev_deleted: bool) -> int:
        if (i, rem, all_prev_deleted) in cache:
            ans = cache[(i, rem, all_prev_deleted)]
        elif i == n:
            if all_prev_deleted:
                if '0' in s:
                    ans = 0
                else:
                    ans = 10 ** 20
            elif rem == 0:
                ans = 0
            else:
                ans = 10 ** 20
        elif int(s[i]) == 0:
            if all_prev_deleted:
                ans = 1 + (yield dp(i + 1, (rem - int(s[i])) % 3, True))
            else:
                ans = yield dp(i + 1, rem, False)
        elif rem == 0:
            ans = 0
        else:
            ans1 = 1 + (yield dp(i + 1, (rem - int(s[i])) % 3, all_prev_deleted))
            ans2 = yield dp(i + 1, rem, False)
            ans = min(ans1, ans2)
        cache[(i, rem, all_prev_deleted)] = ans
        yield ans


    @bootstrap
    def reconstruct(i: int, rem: int, all_prev_deleted: bool) -> int:
        if i == n:
            yield
        elif int(s[i]) == 0:
            if all_prev_deleted:
                yield reconstruct(i + 1, (rem - int(s[i])) % 3, True)
            else:
                t.append(s[i])
                yield reconstruct(i + 1, rem, False)
        elif rem == 0:
            t.extend(list(s[i:]))
            yield
        else:
            ans1 = 1 + cache[(i + 1, (rem - int(s[i])) % 3, all_prev_deleted)]
            ans2 = cache[(i + 1, rem, False)]
            if ans1 < ans2:
                yield reconstruct(i + 1, (rem - int(s[i])) % 3, all_prev_deleted)
            else:
                t.append(s[i])
                yield reconstruct(i + 1, rem, False)
        yield


    s = input()
    n = len(s)
    total = 0
    for num in s:
        num = int(num)
        total += num
    rem = total % 3
    if rem == 0:
        print(s)
        return
    else:
        t = []
        cache = dict()
        if dp(0, rem, True) == 10 ** 20:
            print(-1)
            return
        reconstruct(0, rem, True)
    if t:
        print(''.join(t))
    else:
        print('0')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
