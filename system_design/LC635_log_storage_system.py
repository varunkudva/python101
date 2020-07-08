class LogSystem(object):

    def __init__(self):
        self.logs = []

    @staticmethod
    def _convert_ts(timestamp):
        tstr = timestamp.split(":")
        res = 0
        for i, token in enumerate(tstr):
            if i == 0:
                token = int(token) - 2000
            res = res * 60 + int(token)
        return res

    def put(self, id, timestamp):
        pass

    def retreive(self, s, e, granularity):
        pass


print
LogSystem()._convert_ts("2017:01:01:23:59:59")
put(1, "2017:01:01:23:59:59");
put(2, "2017:01:01:22:59:59");
put(3, "2016:01:01:00:00:00");
