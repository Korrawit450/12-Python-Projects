# Implementation of binary search algorithm!!

# We will prove that binary search is faster than naive search!

# naive search: scan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1
def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED
def binary_search(l, target):
    # example l = [1, 3, 5, 10, 12] # should return 3
    midpoint = (len(l)) // 2 # 2