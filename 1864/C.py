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


def least_set_bit(n: int) -> int:
    """
    least_set_bit(6) -> 2
    """
    return n & -n


def is_power_of_two(n: int) -> bool:
    return n & (n - 1) == 0


def solution():
    x = int(input())
    k = 1
    ans = [x]
    while not is_power_of_two(x):
        k += 1
        d = least_set_bit(x)
        x -= d
        ans.append(x)
    while x != 1:
        k += 1
        x //= 2
        ans.append(x)
    print(k)
    print(*ans)





def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
