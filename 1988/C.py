from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    cur = n
    ans = [cur]
    cur = n & (n - 1)
    if cur > 0:
        ans.append(cur)
        found = True
        while found:
            found = False
            k = 0
            while k < 64:
                if n & 1 << k > 0 and cur & 1 << k == 0:
                    j = k + 1
                    while j < 64:
                        if n & 1 << j > 0 and cur & 1 << j > 0:
                            cur |= 1 << k
                            cur &= ~(1 << j)
                            ans.append(cur)
                            found = True
                            break
                        j += 1
                    if found:
                        break
                k += 1
    print(len(ans))
    print(*reversed(ans))



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
