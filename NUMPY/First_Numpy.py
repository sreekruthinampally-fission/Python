import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))

#1
arr2 = np.array(42)
print(arr2)

arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3)

arr4 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr4)

print(arr4.ndim)

arr5 = np.array([1,2,3,4], ndmin = 5)
print(arr5)
print(arr5.ndim)

arr6 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr6)
print("The element of the second row and third column is : ", arr6[1,2])
print("The element on the first row, fifth column is : ", arr6[0,4])

arr7 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr7)
print(arr7[0,1,2])

arr8 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr8)
print(arr8[1,-1])

