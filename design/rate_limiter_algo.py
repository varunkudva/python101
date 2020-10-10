"""
This implements the token bucket algorithm for ratelimiting
"""
import time
from collections import defaultdict

def get_current_ms():
    return int(round(time.time() * 1000))

class TokenBucketLimiter(object):

    def __init__(self, capacity, rate):
        """

        :param capacity: Initial capacity
        :param rate: rate of requests per second
        """
        self.max_bucket_size = capacity
        self.cur_bucket_size = self.max_bucket_size
        self.refill_rate = rate
        self.last_refill_ts = get_current_ms()

    def refill(self):
        refill_tokens = ((get_current_ms() - self.last_refill_ts) * self.refill_rate)\
                        // 1000 # ms_per_second
        return refill_tokens

    def allow_request(self):
        """
        Allow or deny a request based on available tokens
        :return: True or False
        """
        self.refill()
        if self.cur_bucket_size > 0:
            self.cur_bucket_size -= 1
            return True
        return False

class ApiCache(object):
    """
    key: api
    value: ratelimiter
    """
    def __init__(self):
        self.api_cache = dict() #

    def get_rate_limiter(self, api):
        rlim = None
        if api in self.api_cache:
            rlim = self.api_cache[api]
        else:
           rlim = self.api_cache[api] = TokenBucketLimiter()
        return rlim

def main():
    client_cache = defaultdict(ApiCache)

    rate_limiter = TokenBucketLimiter(10, 10)
    for reps in range(20):
        print("timestamp: {} allowed {}".format(get_current_ms(), rate_limiter.allow_request()))
        time.sleep(50/1000)

"""
(1) Fetch client identifier and api from request
(2) if no client_id, just use api
client_id = request.get_client_id()
api = request.get_api()
if client_id:
    client_api_cache.get_rate_limiter().allow_request()
 
"""
main()
