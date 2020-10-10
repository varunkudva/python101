"""
https://leetcode.com/problems/logger-rate-limiter/
BF: hashtable with  (log, timestamp)
1st approach: sliding window (queue)
2nd approach: buckets
"""
class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        """
         - delete logs with old timestamp from queue
         - if log in queue:
                update ts
            else:
                add to queue
        """
        while self.queue:
            log, ts = self.queue[0]
            if timestamp - ts >= 10:
                self.queue.pop(0)
            else:
                break

        for item in self.queue:
            log, _ = item
            if log == message:
                return False

        self.queue.append((message, timestamp))
        return True


