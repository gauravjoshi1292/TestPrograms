def find_bad_spots(s):
    bad_spots = []
    for i in range(len(s)-1):
        if i % 2 == 0:
            if s[i] >= s[i+1]:
                # odd
                bad_spots.append(i)
        else:
            if s[i] <= s[i+1]:
                # even
                bad_spots.append(i)
    return bad_spots

def create_swap_points(bad_spots, end):
    swap_points = []
    for i in bad_spots:
        if i == 0:
            swap_points.append(i)
            swap_points.append(i+1)

        elif i == end:
            swap_points.append(i-1)
            swap_points.append(i)

        else:
            swap_points.append(i-1)
            swap_points.append(i)
            swap_points.append(i+1)

    return list(set(swap_points))

def check_if_bad(i, j, s, bad_spots):
    points = list(set([i-1, i, i+1, j-1, j, j+1]))
    # print "points:", points
    # print "s:", s, i, j

    for p in bad_spots:
        if p not in points:
            return False

    for p in points:
        # print p
        if p == len(s)-1:
            p -= 1

        if p >= 0 and p < len(s)-1:
            if p % 2 == 0:
                if s[p] >= s[p+1]:
                    # odd
                    return False
            else:
                if s[p] <= s[p+1]:
                    # even
                   return False
    return True


def main():
    n = int(raw_input())
    t = [int(i) for i in raw_input().split()]
    count = 0

    swaps = set()
    bad_spots = find_bad_spots(t)

    if len(bad_spots) > 4:
        pass

    elif len(bad_spots) == 4:
        swap_points = create_swap_points(bad_spots, len(t)-1)
        for i in range(len(swap_points)-1):
            for j in range(i+1, len(swap_points)):
                idx_a, idx_b = ((swap_points[i], swap_points[j]) if swap_points[i] < swap_points[j] else (swap_points[j], swap_points[i]))
                tmp = t[idx_a]
                t[idx_a] = t[idx_b]
                t[idx_b] = tmp

                if check_if_bad(idx_a, idx_b, t, bad_spots):
                    swaps.add((idx_a, idx_b))
                    count += 1

                tmp = t[idx_a]
                t[idx_a] = t[idx_b]
                t[idx_b] = tmp

    else:
        swap_points = create_swap_points(bad_spots, len(t)-1)
        for i in range(len(swap_points)):
            for j in range(len(t)):
                idx_a, idx_b = ((swap_points[i], j) if swap_points[i] < j else (j, swap_points[i]))
                if idx_a != idx_b:
                    tmp = t[idx_a]
                    t[idx_a] = t[idx_b]
                    t[idx_b] = tmp

                    if check_if_bad(idx_a, idx_b, t, bad_spots):
                        # print "a:", idx_a, "b:", idx_b
                        swaps.add((idx_a, idx_b))
                        count += 1

                    tmp = t[idx_a]
                    t[idx_a] = t[idx_b]
                    t[idx_b] = tmp

    # print swaps
    print len(swaps)
    return

main()
