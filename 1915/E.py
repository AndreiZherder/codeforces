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
    nums = [int(num) for num in input().split()]
    if n == 1:
        print('NO')
        return
    pref1 = [0, nums[0], nums[0]]
    pref2 = [0, 0, nums[1]]
    for i in range(2, n, 2):
        pref1.append(pref1[-1] + nums[i])
        if i + 1 < n:
            pref1.append(pref1[-1])
        pref2.append(pref2[-1])
        if i + 1 < n:
            pref2.append(pref2[-1] + nums[i + 1])
    seen = set()
    for i in range(len(pref1)):
        if pref1[i] - pref2[i] in seen:
            print('YES')
            return
        else:
            seen.add(pref1[i] - pref2[i])
    print('NO')




def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
