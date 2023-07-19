from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    tmp = input()
    grid = []
    for i in range(8):
        grid.append(input())
    for i in range(1, 7):
        for j in range(1, 7):
            if grid[i][j] == '#' and grid[i - 1][j - 1] == '#' and grid[i - 1][j + 1] == '#' and grid[i + 1][j + 1] == '#' and grid[i + 1][j - 1] == '#':
                print(i + 1, j + 1)
                return


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
