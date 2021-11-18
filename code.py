a1 = [2, 1, 4, 5, 3, 6, 7, 7, 19, 19, 19, 19]
print(sorted(a1), len(a1))


def med(p):
    n = len(p)
    if n % 2 == 1:
        return quickselect(p, (n - 1) // 2)
    else:
        return (quickselect(p, (n - 1) // 2) + quickselect(p, 1 + (n - 1) // 2)) / 2


def quickselect(a, k):
    # choose some poor element
    poor = a[-1]
    # devide initial list in three: one with els < than poor, one with els > poor, one with els == poor respectfully
    lesser = [x for x in a if x < poor]
    greater = [x for x in a if x > poor]
    piv = [x for x in a if x == poor]
    if len(lesser) - 1 >= k:  # if so, k-th element is in left part and we apply algorithm to it
        return quickselect(lesser, k)
    elif len(lesser) + len(piv) > k:  # if so, then k-th element == our chosen element and we won
        return poor
    else:  # if so, k-th element is in right part and we apply algorithm to it
        return quickselect(greater, k - len(lesser) - len(piv))


print(med(a1))
