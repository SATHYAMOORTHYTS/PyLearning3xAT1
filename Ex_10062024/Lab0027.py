from queue import PriorityQueue  # ✅ Operators
from xml.dom.minidom import ProcessingInstruction

from PyLearning3xAT.Ex_07062024.Lab0014 import result

# 1. Assignment Operators
 # 2. Arithmetic Operators
 # 3. Comparison (Relational) Operators
 # 4. Logical Operators
 # 5. Bitwise Operators
 # 6. Special Operators
 # 7. Unary operators


 # Unary operators
age = +10
print(age)
num = -65
print(num)
r = age + num #BODMAS - Math
print(r)

#  Not Operator ( Works with booleans)
is_married = True
print(not is_married)

# Is Operator - used in list
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
print(list1 is list2)
print(list1 is not list2)
print(id(list1))
print(id(list2))
a = 5
b = 6
print(a is b)


