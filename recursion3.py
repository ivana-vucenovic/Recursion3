# Given a sorted array and a value, recursively determine whether value is found within array. 

# rBinarySearch([1,3,5,6],4) = false; 
# rBinarySearch([4,5,6,8,12],5) = true
arr = [4,5,6,8,12]
val = 5
def rBinarySearch(arr, val):
    if len(arr) == 0:
        return False
    elif arr[len(arr)-1] == val:
        return True
    else:
        return rBinarySearch(arr[0:len(arr)-1], val)

print(rBinarySearch(arr, val))

# Given two integers, create rGCF(num1,num2) to recursively determine Greatest Common Factor (the largest integer dividing evenly into both). Greek mathematician Euclid demonstrated these facts:

# gcf(a,b) == a, if a == b;
# gcf(a,b) == gcf(a-b,b), if a>b;
# gcf(a,b) == gcf(a,b-a), if b>a.

def rGCF(num1, num2):
    if num1 == num2:
        return num1
    elif num1 > num2:
        return rGCF(num1 - num2, num2)
    else:
        return rGCF(num1, num2 - num1)

print(rGCF(60, 48))




