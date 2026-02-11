import numpy as np
#1
arr = np.array(42)
print(arr)

arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1)

#2
arr2 = np.array([10,20,30,40,50])
print("Mean :", np.mean(arr2))
print("Mean :", np.max(arr2))
print("Mean :", np.min(arr2))

#3

arr3 = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr3[0])
print(arr3[:, 0])

print(arr3[2])
print(arr3[:, 2])

print(arr3[0:2, 1:2])

#4
li = [1,2,3,4]
np_arr = np.array(li)

print(np_arr)

