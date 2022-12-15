from itertools import product
from typing import List




def solution():
    def good(s: List[int]) -> bool:
        cnt = [0, 0]
        for i in range(len(s)):
            if s[i] == 0:
                cnt[0] += 1
            else:
                cnt[1] += 1
            if i % 2 == 0:
                if cnt[int(s[i])] < i // 2 + 1:
                    return False
        return True

    ss = list(product([0, 1], repeat=2))
    print(ss)

    for s in ss:
        s = list(s)
        for i in range(len(s)):
            print('---------------------')
            print(s)
            print('---------------------')
            cnt = 0
            for i in range(len(s)):
                print(s[:i + 1])
                res = good(s[:i + 1])
                print(res)
                if res:
                    cnt += 1
            print('cnt = ', cnt)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
