#!/bin/env python
"""
service A ------- service B
99%                 95%
100                 95, 5
5                   4.75, .25
.25                 .2375, .0125
                    --------------
                    99.9875

1    .95, .05

"""

def num_of_retries(current_availability, target_availability):
    tries = 100
    cur, retry_count = 0, 0
    while cur < target_availability:
        retry_count += tries
        succeeded = tries * current_availability * .01
        cur += succeeded
        tries = tries - succeeded
    return retry_count


print(num_of_retries(90, 99))