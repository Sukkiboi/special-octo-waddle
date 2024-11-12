# CRUD OPERATION
# C=>CREATE
# R=>READ
# U=>UPDATE
# D=>DELETE

# Methods of LIST
# 1]append(): It will add data at the end of list.
#   var.append(value)
# l=[11,22,33,44]
# l.append(55)
# print(l)  [11,22,33,44,55]
# l=[11,22,33,44,[1,2,3,4],55,66]
# l.append(77)
# print(l)  [11,22,33,44,[1,2,3,4],55,66,77]
# l[4].append(5)
# print(l)  [11,22,33,44,[1,2,3,4,5],55,66]


# 2]insert(): To add a data at particular index number
# var.insert(index,value)
# l=[11,22,44,55,66]
# l.insert(2,33)
# print(l)  [11,22,33,44,55,66]
# l=["kunal","sujay",["om","pratiksha",["manoj","aditya","rutuja"],"sakshi"],"snehal"]
# l.insert(4,"payal")
# print(l)  ["kunal","sujay",["om","pratiksha",["manoj","aditya","rutuja"],"sakshi"],"snehal","payal"]
# l.insert(1,"prajwal")
# print(l)  ["kunal","prajwal","sujay",["om","pratiksha",["manoj","aditya","rutuja"],"sakshi"],"snehal"]
# l[2][2].insert(3,"sarvesh")
# print(l)


# how to UPDATE DATA
# by Using
# 1.Indexing
# 2.Slicing
# We can update data by:-
# 1.Indexing: var[index]=uvalue
# l=[11,22,333,44,55]
# l[2]=33
# print(l)  [11,22,33,44,55]

# 2.Slicing: var[start_index:end_index]=uvalue
# l=[11,222,333,44,55]
# l[1:3]=[22,33]
# print(l)  [11,22,33,44,55]

# l=[11,222,333,44,55]
# l[0:5]=["sukanth"]
# print(l) ['sukanth']

# l=[11,222,333,44,55]
# l[0:5]="sukanth"
# print(l)  ['s','u','k','a','n','t','h']

# l=[11,222,333,44,55]
# l[0:5]=[69]  It will not accept only 69 i.e without apostrophe or square bracket as it is not a collection
# print(l)  [69]

# iterables in python (collectives)
# ()=tuple
# []=list
# {}=set
# ""=String


# How to Delete Data:
# by using
# 1] remove() syntax:var.remove(value)
# l=[11,22,33,44,55]
# l.remove(11)
# print(l)  [22,33,44,55] If you have a element repeated multiple times in your list then the remove method will always remove the first element.

# 2] pop() syntax:var.pop(index)
# l=[11,22,33,44,55,22]
# l.pop(-1)
# print(l)  [11,22,33,44,55]
# Default value is it will delete the last element i.e. element with -1 index number
# It gives the deleted value in return.
# f=["dishant","komal","mansi","om"]
# p=["jay","ajay","vijay","sujay","pranav"]
# f.append(p.pop(-1))
# # f.append("pranav")
# print(p)
# print(f)

# student=["Sukanth"]
# student.extend(["vijay"])
# print(student)

# l=[11,22,33,[1,2,3,4,5,[10,20,30,40],5,6],44,55]
# l.remove(55)
# l[3].pop(-2)
# l[3][5].pop(-2)
# l.insert(6,66)
# l.insert(3,333)
# l[3].insert(8,7)
# l[3].insert(3,444)
# l[3][5].insert(2,21)
# print(l)

# index()
# syntax: var.index(value)
# l=[11,22,33,44,55]
# print(l.index(44))  3

# reverse()
# syntax: var.reverse()
# l=[11,22,33,44]
# l.reverse()  it does not return 
# print(l)  [44,33,22,11]

# sort()
# syntax:var.sort()
# l=[22,11,44,33]
# l.sort()
# print(l)  [11,22,33,44]
# l.sort(reverse=True)  Dedault Value is Flase
# print(l)  [44,33,22,11]

# what is difference between sort and sorted
# sort is a method and sorted is a function
# sort does not give in return and sorted gives in return

# l=[22,33,11,44]
#print(sorted(l))  It creates a new object and does not do any changes in the original variable

# copy()
a=["sukanth","ajay","sujay"]
b=a.copy()
# print(b)
b.append("vijay")
print(b)  ["sukanth","ajay","sujay","vijay"]
print(a)  ["sukanth","ajay","sujay"]
