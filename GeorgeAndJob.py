n,m,k = [int(i) for i in raw_input().split()]

x = [int(i) for i in raw_input().split()]

s = []
sum = 0
for i in x:
	sum += i
	s.append(sum)

dp=[]
for i in range(k+1):
	dp.append([])
	for j in range(n):
		dp[i].append(0)

dp[1][m-1] = s[m-1]

for i in range(1,k+1):
	for j in range(m,n):
		dp[i][j] = max(dp[i][j-1], dp[i-1][j-m]+s[j]-s[j-m])

print dp[k][n-1]