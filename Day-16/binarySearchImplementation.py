def binarySearch(lis,target):
    low = 0
    high = len(lis) - 1
    while low <= high:
        mid = (low+high)//2
        if lis[mid] == target:
            return "Element Found"
        elif lis[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "Element Not Found" 
elements = list(map(int,input().split()))
target = int(input())
print(binarySearch(elements,target))