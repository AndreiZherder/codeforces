from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    grid = []
    for i in range(8):
        grid.append(input())
    for i in range(8):
        for j in range(8):
            if grid[i][j] != '.':
                ans = []
                for k in range(i, 8):
                    if grid[k][j] != '.':
                        ans.append(grid[k][j])
                    else:
                        break
                print(''.join(ans))
                return


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
