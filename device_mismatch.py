# coding=utf-8
# !/usr/bin/env python
import datetime
import json
from collections import defaultdict

import pandas as pd

# DHCP_STATE_FILE ='/Users/vkudva/devicecache/debug-dhcp-state.log'
# DHCP_ENDPOINT_FILE = '/Users/vkudva/devicecache/debug-dhcp-endpoint.log'
EP = 'dhcp_ep'
STATE = 'dhcp_state'
DHCP_STATE_FILE = '/Users/vkudva/devicecache/test/dhcp_state'
DHCP_ENDPOINT_FILE = '/Users/vkudva/devicecache/test/dhcp_endpoints'


def flattern_endpoint():
    pass


def flatten_state():
    pass


def find_mismatch():
    endpoints = defaultdict(dict)
    dhcp_state = dict()
    no_state_list = []
    mismatch_hname_list = []
    mismatch_opt60_list = []

    # Read dhcp endpoints
    with open(DHCP_ENDPOINT_FILE) as fd:
        for line in fd:
            obj = json.loads(line)
            for k, v in obj.items():
                v.update({x: y for (x, y) in v['fingerprint']['dhcp'].items()})
                str_time = datetime.datetime.fromtimestamp(int(v['updateTime'])).strftime('%c')
                v['updateTime'] = str_time
                del (v['fingerprint'])
                endpoints[k].update({EP: v})
    # print(endpoints)

    with open(DHCP_STATE_FILE) as fd:
        for line in fd:
            obj = json.loads(line)
            for k, v in obj.items():
                if 'options' in v:
                    v.update({x: y for (x, y) in v['options'].items()})
                    del (v['options'])
                if 'protoState' in v:
                    str_time = datetime.datetime.fromtimestamp(v['protoState']['lastseen'] // 1000000).strftime('%c')
                    # v.update({'lastseen': v['protoState']['lastseen']//1000000})
                    v.update({'lastseen': str_time})
                    del (v['protoState'])
                # add mac
                v.update({'mac': k})
                endpoints[k].update({STATE: v})

    for mac, obj in endpoints.items():
        if EP in obj and STATE not in obj:
            no_state_list.append(obj)
        if EP in obj and STATE in obj:
            ep = obj[EP]
            st = obj[STATE]
            # 1. hostname not matching
            try:
                ep_hname = ep.get('hostname', None)
                st_hname = st.get('hostname', None)
                # if type(st_hname) is list:
                #     st_hname = st_hname[0]
                if ep_hname and st_hname:
                    if ep_hname != st_hname:
                        mismatch_hname_list.append(obj)
                else:
                    if ep_hname is None and st_hname is None:
                        continue
                    mismatch_hname_list.append(obj)
            except Exception as e:
                mismatch_hname_list.append(obj)
                pass

            # 2. option 60 not matching
            # try:
            #     ep_opt60 =

    for items in mismatch_hname_list:
        # print(items[EP], items[STATE])
        df = pd.DataFrame(items)
        print(df)

    # print(*mismatch_hname_list, sep = '\n')

    # 2. acp_ips not matching:


if __name__ == '__main__':
    find_mismatch()
