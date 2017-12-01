def update_gap(gap):
    gap = (gap * 10) / 13
    if gap == 9 or gap == 10:
        gap = 11
    return int(max(1, gap))

def combsort(x):
    gap = len(x)
    swapped = True
    if gap < 2:
        return
    while gap > 1 or swapped:
        gap = update_gap(gap)
        swapped = False
        for i in range(0, len(x) - gap, gap):
            if x[i] > x[i + gap]:
                x[i], x[i + gap] = x[i + gap], x[i]
                swapped = True