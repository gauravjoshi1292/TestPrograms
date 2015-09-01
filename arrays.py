__author__ = 'gjoshi'

n1, n2 = map(int, raw_input().split())
k, m = map(int, raw_input().split())

s = raw_input()
a = [int(i) for i in s.split()]

s = raw_input()
b = [int(i) for i in s.split()]

if a[k-1] < b[-m]:
    print("YES")
else:
    print("NO")
