def solution():
    n = int(input())
    s = input()
    x, y = 0, 0
    for c in s:
        if c == 'R':
            x += 1
        elif c == 'L':
            x -= 1
        elif c == 'U':
            y += 1
        else:
            y -= 1
        if x == 1 and y == 1:
            print('YES')
            return
    print('NO')




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
