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
    s = input()
    pref = [n - 1 for i in range(n)]
    for i in range(n - 2, -1, -1):
        if s[i] >= s[pref[i + 1]]:
            pref[i] = i
        else:
            pref[i] = pref[i + 1]
    subseq = []
    i = 0
    while i != n:
        subseq.append(pref[i])
        i = pref[i] + 1
    s1 = list(s)
    i = 0
    j = len(subseq) - 1
    while i < j:
        s1[subseq[i]], s1[subseq[j]] = s1[subseq[j]], s1[subseq[i]]
        i += 1
        j -= 1
    if all(s1[i] >= s1[i - 1] for i in range(1, n)):
        cnt = 0
        for i in subseq:
            if s[i] == s[subseq[0]]:
                cnt += 1
        print(len(subseq) - (cnt - 1) - 1)
    else:
        print(-1)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
