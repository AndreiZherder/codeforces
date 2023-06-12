import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    q = int(input())
    xs = [int(num) for num in input().split()]
    state = 1
    ans = ['1']
    stack = [xs[0]]
    for x in xs[1:]:
        if state == 1:
            if x >= stack[-1]:
                ans.append('1')
                stack.append(x)
            else:
                if x <= stack[0]:
                    ans.append('1')
                    stack.append(x)
                    state = 2
                else:
                    ans.append('0')
        else:
            if stack[-1] <= x <= stack[0]:
                ans.append('1')
                stack.append(x)
            else:
                ans.append('0')
    print(''.join(ans))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
