import sys

input = sys.stdin.readline
print_list = lambda arr: sys.stdout.write(" ".join(map(str, arr)) + "\n")



def solution():
    n = int(input())
    a = [int(num) for num in input().split()]



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
