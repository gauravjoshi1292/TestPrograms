__author__ = 'gjoshi'

s = raw_input()
n, d = int(s.split()[0]), int(s.split()[1])

buy_list = {}
sell_list = {}

for i in range(n):
    s = raw_input()
    if s.split()[0] == 'B':
        try:
            buy_list[int(s.split()[1])] += int(s.split()[2])
        except KeyError:
            buy_list[int(s.split()[1])] = int(s.split()[2])
    else:
        try:
            sell_list[int(s.split()[1])] += int(s.split()[2])
        except KeyError:
            sell_list[int(s.split()[1])] = int(s.split()[2])

top_buys = sorted(buy_list.items(), key=lambda x: x[0], reverse=True)[:d]
top_sells = sorted(sorted(sell_list.items(), key=lambda x: x[0])[:d], key=lambda x: x[0], reverse=True)

for i in top_sells:
    print "S {0} {1}".format(i[0], i[1])

for i in top_buys:
    print "B {0} {1}".format(i[0], i[1])
