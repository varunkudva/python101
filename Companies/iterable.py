"""

"""
import unittest


class Call:
    def __init__(self, start, end, volume):
        self.start = start
        self.end = end
        self.volume = volume

    def __lt__(self, other):
        return self.start < other.start

    def __repr__(self):
        return "({},{},{})".format(self.start, self.end, self.volume)


class Solution:
    def phone_calls(self, start, duration, volume, argument):
        switcher = {
            'brute_force': self.phone_calls_brute_force,
            'dp': self.phone_calls_dp,
            'greedy': self.phone_calls_greedy,
        }
        return switcher.get(argument)(start, duration, volume)

    def phone_calls_brute_force(self, start, duration, volume):
        end = [start[i] + duration[i] for i in range(len(start))]
        calls = []
        for s, e, v in zip(start, end, volume):
            calls.append(Call(s, e, v))

        def overlapping(c1, c2):
            return c1.start < c2.end and c2.start < c1.end

        # sort based on start time
        calls = sorted(calls)
        max_volume, cur_volume = 0, 0
        """
        O(n2) brute force solution. pick every interval and combine with other non
        overlapping intervals. Finally pick the max of all the combinations
        """
        for i in range(len(calls)):
            cur_volume = calls[i].volume
            last_index = i
            for j in range(i + 1, len(calls)):
                if not overlapping(calls[last_index], calls[j]):
                    last_index = j
                    cur_volume += calls[j].volume
            max_volume = max(max_volume, cur_volume)

        return max_volume

    def phone_calls_dp(self, start, duration, volume):
        end = [start[i] + duration[i] for i in range(len(start))]
        # call object with have (start, end, volume)
        calls = []
        for s, e, v in zip(start, end, volume):
            calls.append(Call(s, e, v))

        # sort based on start time
        n = len(calls)
        calls = sorted(calls)

        # volume_agg[i] = max(volume_agg[i-1], volume_agg[i] + volume_agg[j] where j<i and j.end < i.start)
        volume_agg = [0] * n
        volume_agg[0] = calls[0].volume
        for i in range(1, n):
            volume_without_call_i = volume_agg[i - 1]
            volume_with_call_i = calls[i].volume

            # if this call is included in max, find a non overlapping call from
            # earlier calls and add to volume
            for prev in range(i - 1, -1, -1):
                if calls[prev].end < calls[i].start:
                    volume_with_call_i += volume_agg[prev]
                    break
            print(volume_agg)
            volume_agg[i] = max(volume_with_call_i, volume_without_call_i)

        return max(volume_agg)

    def phone_calls_greedy(self, start, end, volume):
        pass


class TestSolution(unittest.TestCase):
    def test_sample_1_brute_force(self):
        start = [5, 10, 15, 18, 30]
        # end    = [17, 40, 35, 53, 65]
        duration = [12, 30, 20, 35, 35]
        volume = [51, 50, 20, 25, 10]
        self.assertEqual(76, Solution().phone_calls(start, duration, volume, 'brute_force'))

    def test_sample_2_brute_force(self):
        start = [5, 10, 15, 18, 30]
        # end    = [12, 40, 35, 53, 65]
        duration = [7, 30, 20, 35, 35]
        volume = [51, 56, 20, 25, 10]
        self.assertEqual(71, Solution().phone_calls(start, duration, volume, 'brute_force'))

    def test_sample_1_dp(self):
        start = [5, 10, 15, 18, 30]
        # end    = [17, 40, 35, 53, 65]
        duration = [12, 30, 20, 35, 35]
        volume = [51, 50, 20, 25, 10]
        self.assertEqual(76, Solution().phone_calls(start, duration, volume, 'dp'))

    def test_sample_2_dp(self):
        start = [5, 10, 15, 18, 30]
        # end    = [12, 40, 35, 53, 65]
        duration = [7, 30, 20, 35, 35]
        volume = [51, 56, 20, 25, 10]
        self.assertEqual(76, Solution().phone_calls(start, duration, volume, 'dp'))


if __name__ == '__main__':
    unittest.main(verbosity=3)
