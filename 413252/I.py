from collections import defaultdict


def solution():
    def yolka(node: int) -> bool:
        if not tree[node]:
            return True
        cnt = 0
        for child in tree[node]:
            if not tree[child]:
                cnt += 1
            else:
                res = yolka(child)
                if not res:
                    return False
        return cnt >= 3

    n = int(input())
    tree = defaultdict(list)
    for i in range(2, n + 1):
        tree[int(input())].append(i)
    if yolka(1):
        print('Yes')
    else:
        print('No')



t = 1
while t:
    solution()
    t -= 1