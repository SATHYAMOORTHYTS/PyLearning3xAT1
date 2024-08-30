#sets
# List of items in a collection that are unordered and unique
#
my_set = {1,2,3,4,5,5}

# sets are ordered in {} curly braces

my_set2 = {1,24,3,43,5,5}#- remove the duplicates and convert into correct order
my_set1 = {1,2,3,4,5,5}

my_set = my_set1.intersection (my_set2)
print(my_set)

my_set = my_set1.union(my_set2)
print(my_set)

my_set = my_set1.difference(my_set2)
print(my_set)

#

my_set1 = {1,2,3,4,5,6}
my_set2 = {2,4,5}

subset = my_set1.issubset(my_set2)
print(subset)








