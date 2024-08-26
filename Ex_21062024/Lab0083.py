# x = 10
# q, w, e = (23, 22, 33,)
#
# print(x)
# print(q)
# print(w)
#
#
# # search in tuple
# tuple1 = ("london",  "paris", "tokyo", "new york")
# print("paris" in tuple1)
# print("shanghai" in tuple1)

t = (1,2,3,4,5,)
#t.append() tuple are immutable in nature
new_t = t + (11,) # append - we can add another element in the tuple
print(new_t)

my_list = list(t)
print(my_list)
my_list.append(11)
my_list.append(22)
print(my_list)
new_t2 = tuple(my_list)
print(new_t2)
