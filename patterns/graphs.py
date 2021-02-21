class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        hit: hot
        hot: dot, lot
        """

        def similar(w1, w2):
            count = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    count += 1
            return True if count <= 1 else False

        if endWord not in wordList:
            return 0

        'build graph'
        adj = defaultdict(set)
        if beginWord not in wordList:
            wordList.append(beginWord)

        for i in range(len(wordList) - 1):
            src = wordList[i]
            for j in range(i + 1, len(wordList)):
                neigh = wordList[j]
                if similar(src, neigh):
                    adj[src].add(neigh)
                    adj[neigh].add(src)

        for key, val in adj.items():
            print("{}: {}".format(key, val))

        'do bfs to find a path from src to neigh'
        level = dict()
        visited = set()
        queue = [beginWord]
        level[beginWord] = 1
        while queue:
            src = queue.pop(0)
            for neigh in adj[src]:
                if neigh not in visited:
                    visited.add(neigh)
                    level[neigh] = level[src] + 1
                    if neigh == endWord:
                        return level[neigh]
                    queue.append(neigh)
        return 0