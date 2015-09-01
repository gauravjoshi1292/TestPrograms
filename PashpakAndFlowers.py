n = long(raw_input())

a = []

k = raw_input()
k = k.split()

for i in k:
	a.append(long(i))

maxx = max(a)
minn = min(a)

if maxx == minn:
	print maxx-minn, n*(n-1)/2
else:
	x = a.count(maxx)
	y = a.count(minn)
	print maxx-minn, x*y
