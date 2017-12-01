from heapq import merge

def mergesort(w):
    if len(w)<2:
        return w
    else:
        mid=len(w)//2
        return merge(mergesort(w[:mid]), mergesort(w[mid:]))