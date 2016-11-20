def number_needed(a, b):
    a_hash = dict()
    count = 0
    # create hashmap with a's characters
    for c in a:
        if c in a_hash:
            a_hash[c] += 1
        else:
            a_hash[c] = 1

    # Go through characters in b. pop them
    # if the exist. Else add to hash
    for c in b:
        if c in a_hash and a_hash[c] > 0:
            a_hash[c] -= 1
        else:
            count += 1

    for v in a_hash.values():
        count += v

    return count


a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)