n = int(raw_input())

sum = 0.0
a = [int(i) for i in raw_input().split()]

if n<3:
	print 0
else:
	for i in a:
		sum += i

	s = [0]*n

	x = 0.0
	k = 0
	for i in range(n-1,1,-1):
		x += a[i];
		if(x==sum/3.0):
			k += 1
		s[i] = k

	# print s

	ans = 0
	x = 0.0
	for i in range(n-2):
		x += a[i]
		if(x== sum/3.0):
			# print "i = ",i
			ans += s[i+2]

	print ans