class HitCounter(object):
    class HitEntry(object):
        def __init__(self, ts=0, hits=0):
            self.ts = ts
            self.hits = hits

        def __str__(self):
            return "({},{})".format(self.ts, self.hits)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 300
        self.hits = [self.HitEntry() for _ in range(self.capacity)]

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        index = timestamp % self.capacity
        h_ent = self.hits[index]
        if h_ent.ts != timestamp:
            h_ent.ts = timestamp
            h_ent.hits = 1
        else:
            h_ent.hits += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        """ TODO handle out of bounds"""
        total_count = 0
        for h_ent in self.hits:
            if timestamp - h_ent.ts < 300:
                total_count += h_ent.hits
        return total_count
