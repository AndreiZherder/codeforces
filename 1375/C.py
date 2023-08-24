from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    perm = [int(num) for num in input().split()]
    stack = []
    for i in range(n - 1, -1, -1):
        if not stack:
            stack.append(perm[i])
            continue
        elif len(stack) == 1:
            if perm[i] < stack[-1]:
                continue
            else:
                stack.append(perm[i])
        else:
            if perm[i] < stack[-1]:
                while len(stack) > 1 and perm[i] < stack[-1]:
                    stack.pop()

                if len(stack) == 1:
                    if perm[i] < stack[-1]:
                        continue
                    else:
                        stack.append(perm[i])
                else:
                    stack.append(perm[i])

            else:
                stack.append(perm[i])
    if len(stack) == 1:
        print('YES')
    else:
        print('NO')



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
