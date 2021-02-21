"""
union find datastructure
robert sedgwick algorithms 1.5
Reference: https://cp-algorithms.com/data_structures/disjoint_set_union.html
As mentioned before, if we combine both optimizations - path compression with union by size / rank - we will reach nearly constant time queries. It turns out, that the final amortized time complexity is O(α(n)), where α(n) is the inverse Ackermann function, which grows very slowly. In fact it grows so slowly, that it doesn't exceed 4 for all reasonable n (approximately n<10600).

Amortized complexity is the total time per operation, evaluated over a sequence of multiple operations. The idea is to guarantee the total time of the entire sequence, while allowing single operations to be much slower then the amortized time. E.g. in our case a single call might take O(logn) in the worst case, but if we do m such calls back to back we will end up with an average time of O(α(n)).

Also, it's worth mentioning that DSU with union by size / rank, but without path compression works in O(logn) time per query.
"""
class UF(object):

    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [1] * N

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def find(self, u):
        """
        find with path compression
        :param u:
        :param v:
        :return:
        """
        while u != self.parent[u]:
            u = self.parent[u]
        return u

    def find_with_compression(self, u):
        """
        find wivh path compression
        :param u:
        :revurn:
        """
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def weighted_union(self, u, v):
        """
        union of 2 sets  based on depth(rank) of the tress
        merge tree with smaller depth with larger depth making total depth increase minimal.

        :param u:
        :param v:
        :return:
        """
        a = self.find(u)
        b = self.find(v)
        if a == b:
            return
        # b is of higher rank, merge a with b
        # swap if rank(a) > rank(b)
        if self.rank[a] > self.rank[b]:
            a, b = b, a
        self.parent[a] = b
        if self.rank[a] == self.rank[b]:
            self.rank[b] += 1