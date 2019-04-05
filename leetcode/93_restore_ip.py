# coding=utf-8

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def valid_octet(s):
            return int(s) < 256

        def valid_ip_str(octet):
            return octet.count('.') == 3

        def restore_b(res, ipstr, octet, s):
            '''
            for each int in the ip_string
            if substr is valid_octet, append to result

            '''
            print (ipstr, octet)
            if not s:
                if octet:
                    ipstr = '.'.join([ipstr, octet])
                if valid_ip_str(ipstr):
                    res.append(ipstr)
                else:
                    return

            for i in range(len(s)):
                if valid_octet(octet+s[:i+1]):
                    restore_b(res, ipstr, octet+s[:i+1], s[i+1:])

                # if ipstr:
                #     ipstr = '.'.join([ipstr, octet])
                # else:
                #     ipstr=octet
                restore_b(res, ipstr + '.' + octet, '', s[i:])

            return res

        if 12 < len(s) < 4:
            # failed
            return res

        return restore_b(res, '', '', s)


'''
255.255.1
255.25.5.1
25.52.25.1
25.5.22.51
'''
print (Solution().restoreIpAddresses("2552551"))
