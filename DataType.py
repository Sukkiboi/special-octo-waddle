# There are several types of data types in Python.
# They are divided into 2 data types i.e Fundamental and Collective

# 1]Fundamental: a)Int(Integer): 199,34,45 etc
#                b)float(float number): 12.23,68.69,70.0 etc
#                c)complex(complex number): a+bj
#                                           a= real part
#                                           b= imaginary part c=5=10j
#                                           How to access the real part: var.real
#                                           How to access the imaginary part: var.imag 
#                                           real part can be int or float
#                                           imaginary part must be decimal or float
#                                           Integer Number can be represented by=> 1]binary: only 1 and 0 var=0bvlaue eg: num=0b1001 use bin to find any binary representation of any number
#                                                                                  2]octal: only value between 0 and 7 eg:0o1467 use oct to find octal representation of any number.
#                                                                                  3]decimal: value between 0 and 9
#                                                                                  4]hexa-decimal: value between 0 and 9/a and f eg:0x1344ade use hex to find any hexa-decimal representation
#               d)str
#               e)bool=> true or false

# 2]Collective: a)List: It is comma separated values within []
                        # It is ordered, mutable, heterogenous collection of elements where duplicates are allowed.
                        # Ordered: Its sequence does not change i.e. does not change its position.
                        #mutable: Its value can be changed using a method called append wthout changing its ID i.e. in the same variable.
                        #heterogenous: We can store int,float,str,complex,bool,list etc in the list itself.
#                      Syntax: var=[v1,v2,v3]
#                     n1=[10,20,30,40,50]
                    # print(type(n1)) #List

#How to access elements from list: 1]Indexing syntax:var[index]
#                                  l=[22,33,44,55,]  
#                                  print(l[1]) #33
# student=["Rajesh","ajay","Om","kunal"]
# print(student[1])
# print(student[-1])
# print(student[0])
# print(student[0]+student[-1])

# WAP to print multiplication of square of last element.
# A=[1,2,33,44,6,9,69]
# sf=A[0]*A[0]
# sl=A[-1]*A[-1]  1st WAY
# print(sf+sl)

# Ans=A[0]*A[0]+A[-1]*A[-1]  2nd WAY
# print(Ans)

# 2]Slicing
# l=[11,22,33,[44,55,77],88,99]
# print(l[3][1])  #55

# l=[11,22,33,["raj","kumar","rajesh"],99]
# print(l[3][1][1])  #u

# 2]Slicing syntax:var[start_index:end_index:step_value]
# l=[11,22,33,44,55]
# print(l[0:3:1])  #[11,22,33]
# print(l[2:7:1])  #[33,44,55]
# print(l[0:7:2])  #[11,33,55]
# print(l[0:4:3])  #[11,44]  
# l=[11,12,13,14,15,16,17,18,19,20]
# print(l[-5:-2:1])  #[16,17,18]
# print(l[3:0:-1])  #[14,13,12]
# print(l[0:10:2])  #[11,13,15,17,19]
# print(l[1:10:2])  #[12,14,16,18,20]
# print(l[-2:-14:-2]) #[19,17,15,13,11]
# print(l[-1:-14:-2]) #[20,18,16,14,12]

# l=[11,22,33,44,[55,66,77,88],99,100]
# print(l[1:3:1])  #[22,33]
# print(l[4][1:3:1]) #[66,77]

# Cars=["BMW","Tata","Porsche","Suzuki"]
# print(len(Cars))
# print(type(Cars))
# print(Cars[0][0])
# print(Cars[-3:-1])
# Cars[1]="Hyundai"
# print(Cars)
# Cars[1:3]=["Bently"]
# print(Cars)
# Cars.insert(2,"BYD")
# print(Cars)
# Cars.append("BMW")
# print(Cars)
# Bikes=["bajaj","TVS","Honda","BMV"]
# Cars.extend(Bikes)
# print(Cars)

# 
