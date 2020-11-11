class ApiCache(object):
    """
    key: api
    value: ratelimiter
    """

    def __init__(self):
        self.api_cache = dict()  #

    def get_rate_limiter(self, api):
        rlim = None
        if api in self.api_cache:
            rlim = self.api_cache[api]
        else:
            rlim = self.api_cache[api] = TokenBucketLimiter()
        return rlim
