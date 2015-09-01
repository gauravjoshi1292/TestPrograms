def countBits(num):
	retVal = 0
	while num:
		retVal += num & 1
		num >>= 1
	return retVal


n,m,k = [int(i) for i in raw_input().split()]

a = []
while(m):
	i = int(raw_input())
	a.append(i)
	m -= 1

f = int(raw_input())

ans = 0
for i in a:
	c = i^f
	c = countBits(c)
	if(c<=k):
		ans += 1
print ans