NCHOPSTICKS = 5000


diff = [0] * (NCHOPSTICKS + 1)  # smallest differences between chopsticks
chop = [0] * (NCHOPSTICKS + 1)  # chopsticks
badness = [0] * (NCHOPSTICKS + 1)  # badness for each pair of chopsticks

nc = int(input())  # number of chopsticks

for t in range(nc):
    c = input().split()
    nge = int(c[0])  # number of guests
    nch = int(c[1])  # number of cases
    nge += 8   # add family members
    diff[0] = 0

    c = input().split()

    # Initialize badness as square of the difference of adjacent chopsticks
    for i in range(nch):
        chop[i+1] = int(c[i])
        diff[i+1] = 0
        badness[i+1] = pow(chop[i+1] - chop[i], 2)

    # Dynamic Programming
    for i in range(1, nge+1):
        for j in range(nch - 3*(nge-i) - 1, 2*i - 1, -1):
            diff[j] = diff[j-2] + badness[j]

        # find the neighbouring pairs with smallest difference
        for j in range((2*i) + 1, (nch - 3*(nge-i) - 1) + 1):
            if diff[j-1] < diff[j]:
                diff[j] = diff[j-1]

        # the third chopstick
        diff[nch - 3*(nge-i)] = diff[nch - 3*(nge-i) - 1]

    print(diff[nch])