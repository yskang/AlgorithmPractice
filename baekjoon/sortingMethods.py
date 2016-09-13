def quickSort(xs):
    if len(xs) <= 1:
        return xs

    pivot = xs[len(xs)-1]

    less = []
    more = []
    equal = []

    for x in xs:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            more.append(x)
        else:
            equal.append(x)

    return quickSort(less) + equal + quickSort(more)

def mergeSort(xs):
    if len(xs) <= 1:
        return xs

    mid = len(xs) // 2
    lefts = mergeSort(xs[:mid])
    rights = mergeSort(xs[mid:])

    result = []
    l = 0
    r = 0

    while l < len(lefts) and r < len(rights):
        if lefts[l] < rights[r]:
            result.append(lefts[l])
            l += 1
        else:
            result.append(rights[r])
            r += 1
    
    result += lefts[l:]
    result += rights[r:]
    return result
