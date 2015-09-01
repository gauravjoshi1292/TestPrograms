n = int(raw_input())

ans = 0
for i in range(n):
	p,q = (int(j) for j in raw_input().split())
	if q-p > 1:
		ans+=1

print ans