def printTwoElements( arr, size):
    for i in range(size):
        if arr[abs(arr[i])-1] > 0:
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        else:
            print("The repeating element is",abs(arr[i]))
             
    for i in range(size):
        if arr[i]>0:
            print("and the missing element is",i+1)
 
# Driver program to test above function */
arr = [7, 3, 4, 5, 5, 6, 3]
n = len(arr)
printTwoElements(arr, n)
