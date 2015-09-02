dp = {}
count = 0
n, q = (int(i) for i in raw_input().split())

for i in range(q):
    a, b = raw_input().split()
    dp[a] = b

def compression(s):
    # print "comp:", s
    if len(s) == 1:
        return s

    return dp[s]


def collapse(s):
    # print "s:", s
    if len(s) == 1:
        return s

    if len(s) == 2:
        try:
            return compression(s)
        except KeyError:
            return s

    try:
        cs = compression(s[:2]) + (s[2:])
        if len(cs) < len(s):
            return collapse(cs)
        else:
            return s
    except KeyError:
        return s

y = set(['a', 'b', 'c', 'd', 'e', 'f'])

for i in range(1, n):
    y_cp = y.copy()
    # print dp, dp_cp
    # print "i:", i
    for key in y_cp:
        for c in ['a', 'b', 'c', 'd', 'e', 'f']:
            for j in range(len(key)+1):
                # print "j:", j, c
                new_key = key[:j] + c + key[j:]
                val = collapse(new_key)
                # print new_key, val
                if val:
                    dp[new_key] = val
                y.add(new_key)

for key, val in dp.items():
    if len(key) == n and val == 'a':
        count += 1

print count
