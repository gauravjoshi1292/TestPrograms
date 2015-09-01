s = raw_input()
n,k,d = [int(i) for i in s.split()]

if n > pow(k,d):
	print -1
else:
	s = []
	for i in range(d):
		s.insert(0, [])
	

	for i in range(n):
		a = []
		n = i
		while(n):
			r = n % k + 1
			a = [r,] + a
			n = n/k
		while len(a) < d:
			a = [1,] + a
		for j in range(len(a)):
			s[j].append(a[j])

	for i in s:
		for j in i:
			print j,
		print