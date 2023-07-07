from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    def check(c: str) -> bool:
        for i in range(3):
            if all(grid[i][j] == c for j in range(3)):
                return True
        for j in range(3):
            if all(grid[i][j] == c for i in range(3)):
                return True
        if all(grid[i][i] == c for i in range(3)):
            return True
        if all(grid[i][2 - i] == c for i in range(3)):
            return True
        return False

    grid = []
    for i in range(3):
        grid.append(input())
    if check('X'):
        print('X')
        return
    if check('O'):
        print('O')
        return
    if check('+'):
        print('+')
        return
    print('DRAW')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
