# Sets
# Sets are useful when you need to work with collection unique elements

my_set = {1,2,3,4,5}
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

set1 = {2,4,6}
set2 = {8,10 ,12}

# find the union of set1 and set2( all unique elements from both sets)
union_set = set1.union(set2)
print(union_set)

# find the intersection of set1 and set2(common elements)
inter_set = set1.intersection(set2)
print(inter_set)

# find difference
diff_set = set1.difference(set2)
print(diff_set)
