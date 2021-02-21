"""
You are given a string that contains alphabetical characters (a - z, A - Z) and some other characters ($, !, etc.). For example, one input may be:

'sea!$hells3'

Can you reverse only the alphabetical ones?

reverseOnlyAlphabetical('sea!$hells3');
// 'sll!$ehaes3'
"""
def is_alpha(char):
    if ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z'):
        return True
    return False

def reverse_alphabetical(s):
    start, end = 0, len(s)-1
    slist = list(s)
    while start < end:
        if is_alpha(slist[start]) and is_alpha(slist[end]):
            slist[start], slist[end] = slist[end], slist[start]
            start += 1
            end -= 1
        else:
            if not is_alpha(slist[start]):
                start += 1
            if not is_alpha(slist[end]):
                end -= 1
    return "".join(slist)

print(reverse_alphabetical('sea!$hells3'))
assert (reverse_alphabetical('sea!$hells3') == 'sll!$ehaes3')