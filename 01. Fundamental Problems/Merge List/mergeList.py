def mergeList(first, second):
    combined = first + second
    combined.sort()
    return combined


group1 = [11, 13, 18, 17, 56]
group2 = [12, 15, 19, 43, 66]
merged = mergeList(group1, group2)
print(merged)
