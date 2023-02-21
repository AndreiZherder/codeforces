import sys
from bisect import bisect_left
from copy import deepcopy
from itertools import chain, combinations
from math import gcd
from typing import List

M = 1000000007
mod = 998244353


def input_interactive(*args):
    print(' '.join(chain('?', map(str, args))))
    sys.stdout.flush()
    return input()


def print_interactive(*args):
    print(' '.join(chain('!', map(str, args))))
    sys.stdout.flush()


"""
Binary tricks
"""
# -x = ~x + 1
# ~x = -x - 1
# x & (x - 1)   sets the last one bit to zero
# x & -x        sets all one bits to zero, except the last one bit
# x | (x - 1)   sets all bits to one after the last one bit


def dec_to_bin(x: int, n: int) -> str:
    return bin(x)[2:].zfill(n)


def bin_to_dec(n: str) -> int:
    return int(n, 2)


def set_bits_count(n: int) -> int:
    """
    Count set bits in an integer
    """
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0F0F0F0F0F0F0F0F) + ((c >> 4) & 0x0F0F0F0F0F0F0F0F)
    c = (c & 0x00FF00FF00FF00FF) + ((c >> 8) & 0x00FF00FF00FF00FF)
    c = (c & 0x0000FFFF0000FFFF) + ((c >> 16) & 0x0000FFFF0000FFFF)
    c = (c & 0x00000000FFFFFFFF) + ((c >> 32) & 0x00000000FFFFFFFF)
    return c


def least_set_bit(n: int) -> int:
    """
    least_set_bit(6) -> 2
    """
    return n & -n


def is_power_of_two(n: int) -> bool:
    return n & (n - 1) == 0


def get_subsets(x: int) -> List[int]:
    """
    get all subsets of set x
    """
    ans = []
    b = 0
    while b != x:
        b = (b - x) & x
        ans.append(b)
    return ans


def gcd_small(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def gcd_big(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    k = 0
    while ((a | b) & 1) == 0:
        a = a >> 1
        b = b >> 1
        k = k + 1
    while (a & 1) == 0:
        a = a >> 1
    while b != 0:
        while (b & 1) == 0:
            b = b >> 1
        if a > b:
            a, b = b, a
        b = b - a
    return a << k


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def sieve(n: int):
    """
    Primes <= n
    """
    primes = bytearray(n + 1)
    p = 3
    while p * p <= n:
        if not primes[p]:
            primes[p * p::p] = [1] * len(primes[p * p::p])
        p += 2
    if n >= 2:
        yield 2
    for p in range(3, n + 1, 2):
        if not primes[p]:
            yield p


def prime_factors(n: int):
    """
    Prime factors of n
    prime_factors(99) --> 3 3 11
    """
    while n % 2 == 0:
        yield 2
        n //= 2
    p = 3
    while p * p <= n:
        quotient, reminder = divmod(n, p)
        if reminder == 0:
            yield p
            n = quotient
        else:
            p += 2
    if n != 1:
        yield n


def is_prime(n: int):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    # all primes > 3 are of the form 6n ± 1
    p = 5
    while p * p <= n:
        if n % p == 0:
            return False
        if n % (p + 2) == 0:
            return False
        p += 6
    return True


def factors(n: int):
    """
    Distinct factors of n
    """
    stack = []
    yield 1
    if n != 1:
        stack.append(n)
    p = 2
    while p * p <= n:
        quotient, reminder = divmod(n, p)
        if reminder == 0:
            yield p
            if quotient != p:
                stack.append(quotient)
        p += 1
    while stack:
        yield stack.pop()


def ncr(n: int, r: int, mod: int) -> int:
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * (i + 1)) % mod
    return (num * pow(den, mod - 2, mod)) % mod


def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def lis(nums) -> int:
    """
    Longest increasing subsequence
    """
    dp = []
    for num in nums:
        i = bisect_left(dp, num)
        if i == len(dp):
            dp.append(num)
        else:
            dp[i] = num
    return len(dp)


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        id1 = self.find(i)
        id2 = self.find(j)
        if id1 == id2:
            return
        if self.rank[id1] > self.rank[id2]:
            self.parent[id2] = id1
        else:
            self.parent[id1] = id2
            if self.rank[id1] == self.rank[id2]:
                self.rank[id2] += 1


# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/RangeQuery.py
class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

    def __getitem__(self, idx):
        return self._data[0][idx]


# https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/fenwick_tree.py
class FenwickTree:
    """
    Fenwick Tree
    More info: https://en.wikipedia.org/wiki/Fenwick_tree
    """

    def __init__(self, arr: List[int] = None, size: int = None) -> None:
        """
        Constructor for the Fenwick tree
        Parameters:
            arr (list): list of elements to initialize the tree with (optional)
            size (int): size of the Fenwick tree (if arr is None)
        """

        if arr is None and size is not None:
            self.size = size
            self.tree = [0] * size
        elif arr is not None:
            self.init(arr)
        else:
            raise ValueError("Either arr or size must be specified")

    def init(self, arr: List[int]) -> None:
        """
        Initialize the Fenwick tree with arr in O(N)
        Parameters:
            arr (list): list of elements to initialize the tree with
        Returns:
            None
        >>> a = [1, 2, 3, 4, 5]
        >>> f1 = FenwickTree(a)
        >>> f2 = FenwickTree(size=len(a))
        >>> for index, value in enumerate(a):
        ...     f2.add(index, value)
        >>> f1.tree == f2.tree
        True
        """
        self.size = len(arr)
        self.tree = deepcopy(arr)
        for i in range(1, self.size):
            j = self.next_(i)
            if j < self.size:
                self.tree[j] += self.tree[i]

    def get_array(self) -> List[int]:
        """
        Get the Normal Array of the Fenwick tree in O(N)
        Returns:
            list: Normal Array of the Fenwick tree
        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> f.get_array() == a
        True
        """
        arr = self.tree[:]
        for i in range(self.size - 1, 0, -1):
            j = self.next_(i)
            if j < self.size:
                arr[j] -= arr[i]
        return arr

    @staticmethod
    def next_(index: int) -> int:
        return index + (index & (-index))

    @staticmethod
    def prev(index: int) -> int:
        return index - (index & (-index))

    def add(self, index: int, value: int) -> None:
        """
        Add a value to index in O(lg N)
        Parameters:
            index (int): index to add value to
            value (int): value to add to index
        Returns:
            None
        >>> f = FenwickTree([1, 2, 3, 4, 5])
        >>> f.add(0, 1)
        >>> f.add(1, 2)
        >>> f.add(2, 3)
        >>> f.add(3, 4)
        >>> f.add(4, 5)
        >>> f.get_array()
        [2, 4, 6, 8, 10]
        """
        if index == 0:
            self.tree[0] += value
            return
        while index < self.size:
            self.tree[index] += value
            index = self.next_(index)

    def update(self, index: int, value: int) -> None:
        """
        Set the value of index in O(lg N)
        Parameters:
            index (int): index to set value to
            value (int): value to set in index
        Returns:
            None
        >>> f = FenwickTree([5, 4, 3, 2, 1])
        >>> f.update(0, 1)
        >>> f.update(1, 2)
        >>> f.update(2, 3)
        >>> f.update(3, 4)
        >>> f.update(4, 5)
        >>> f.get_array()
        [1, 2, 3, 4, 5]
        """
        self.add(index, value - self.get(index))

    def prefix(self, right: int) -> int:
        """
        Prefix sum of all elements in [0, right) in O(lg N)
        Parameters:
            right (int): right bound of the query (exclusive)
        Returns:
            int: sum of all elements in [0, right)
        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> res = True
        >>> for i in range(len(a)):
        ...     res = res and f.prefix(i) == sum(a[:i])
        >>> res
        True
        """
        if right == 0:
            return 0
        result = self.tree[0]
        right -= 1  # make right inclusive
        while right > 0:
            result += self.tree[right]
            right = self.prev(right)
        return result

    def query(self, left: int, right: int) -> int:
        """
        Query the sum of all elements in [left, right) in O(lg N)
        Parameters:
            left (int): left bound of the query (inclusive)
            right (int): right bound of the query (exclusive)
        Returns:
            int: sum of all elements in [left, right)
        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> res = True
        >>> for i in range(len(a)):
        ...     for j in range(i + 1, len(a)):
        ...         res = res and f.query(i, j) == sum(a[i:j])
        >>> res
        True
        """
        return self.prefix(right) - self.prefix(left)

    def get(self, index: int) -> int:
        """
        Get value at index in O(lg N)
        Parameters:
            index (int): index to get the value
        Returns:
            int: Value of element at index
        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> res = True
        >>> for i in range(len(a)):
        ...     res = res and f.get(i) == a[i]
        >>> res
        True
        """
        return self.query(index, index + 1)

    def rank_query(self, value: int) -> int:
        """
        Find the largest index with prefix(i) <= value in O(lg N)
        NOTE: Requires that all values are non-negative!
        Parameters:
            value (int): value to find the largest index of
        Returns:
            -1: if value is smaller than all elements in prefix sum
            int: largest index with prefix(i) <= value
        >>> f = FenwickTree([1, 2, 0, 3, 0, 5])
        >>> f.rank_query(0)
        -1
        >>> f.rank_query(2)
        0
        >>> f.rank_query(1)
        0
        >>> f.rank_query(3)
        2
        >>> f.rank_query(5)
        2
        >>> f.rank_query(6)
        4
        >>> f.rank_query(11)
        5
        """
        value -= self.tree[0]
        if value < 0:
            return -1

        j = 1  # Largest power of 2 <= size
        while j * 2 < self.size:
            j *= 2

        i = 0

        while j > 0:
            if i + j < self.size and self.tree[i + j] <= value:
                value -= self.tree[i + j]
                i += j
            j //= 2
        return i


# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/SegmentTree.py
class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/LazySegmentTree.py
class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * _size)

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazy[idx] = self._lazy[idx], 0

        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=0):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)


# based on https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Trie.py
class Trie:
    def __init__(self, *words):
        self.root = {}
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict["_end_"] = True

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_end_" in current_dict

    def startswith(self, prefix):
        current_dict = self.root
        for letter in prefix:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return True
