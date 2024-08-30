set1 = set(["sathya.", " is for", "sathya"])

print(len(set1))

for i in set1:
    print(i)

set1 = set(["sathya.", " is for", "sathya","sathya", " is for", "sathya"])
print(set1)
set1.add("sandhya")
set1.remove("sathya")
print(set1)

set1 = {1,3,4,4,5}
set2 = {2,3,4,5,6}
my_set  = set1.union(set2)
print(my_set)
my_set = set1.intersection(set2)
print(my_set)
my_set = set1.difference(set2)
print(my_set)
my_set = set2.difference(set1)
print(my_set)

# sets are used to add,remove,intersection,union,

set1.remove(3)
print(set1)
set1.discard(3)
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)
