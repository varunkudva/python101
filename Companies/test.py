
start = "RXXLRXRXL", end = "XRLXXRRLX"

def transform(s, t):
    mapping = { 'XL': 'LX',
                'RX': 'XR'}
    if len(s) != len(t):
        return False
    for i in range(len(s)-2):
        if s[i:i+2] != t[i:i+2] or mapping[s[i:i+2]] != t[i:i+2]:
            return False
    return True

transform(start, end)


