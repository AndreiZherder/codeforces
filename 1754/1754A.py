def solution():
    n = int(input())
    s = input()
    stack = []
    for c in s:
        if c == 'Q':
            stack.append(c)
        else:
            if stack:
                stack.pop()
    if stack:
        print('NO')
    else:
        print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
