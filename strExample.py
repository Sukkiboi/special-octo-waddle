'''str:str() is a built-in function in the Python programming language that is used to convert the specified value into a string datatype.'''

# 1]Indexing
# object="rameshwaram"
# print(object[-1])  #m
# print(object[0])   #r
# print(object[6])   #w
# print(object[-11]) #r
# print(object[-6])  #h


'''2]Slicing:When we have to fetch multiple characters
  var[start_index:end_index:step_index]
    start_index:slicing will start from start index.
    end_index:slicing will stop before end index.'''

# name="Facebook"
# print(name[0:4:1])  #Face
# print(name[-4:-1:-1])

#  name="instagram"
# print(name[-4:9:1])  #gram
# print(name[-6:15:1]) #tagram
# name="bhushan"
# print(name[-2:0:-2])  #ash
# start index: If we don't give any start index it starts from the 1st letter or the last letter depending on the step value we give.
# print(name[:3:1])    #bhu
# print(name[:-5:-1])  #nahs

# end index: If we don't give any index number it starts from the 1st letter or the last letter depending on the step value we give.
#step value: If we don't give any step value it'll stat going forward i.e. from left to right.
# So only give the step value if you have to 2 steps,etc or backwards.

# name='rameshwaram'
# print(name[:3])  #ram
# print(name[:-4:-1])  #mar
# print(name[-3::])   #ram
# print(name[2::-1])  #mar

name='pavankumar'
print(name[-5::])  #kumar
print(name[:5])    #pavan
print(name[:-6:-1])#ramuk
print(name[4::-1]) #navap










