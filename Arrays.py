import array as arr
array_num=arr.array('i',[1,3,4,5,6,7,8])
print("Original array:  " +str(array_num))
print("Number of occurences of the element 3 in the said array:  "+str (array_num.count(3)))
array_num.reverse()
print("The reversed order of the array:  ")
print(str(array_num))