import heapq
lis = [5,1,6,4,10,2]
k = 1
#heapq.heapify(lis)
print(lis)
kthLargestElement = heapq.nlargest(k,lis)
kthSmallestElement = heapq.nsmallest(k,lis)
print("kthLargestElement is", kthLargestElement[k-1])
print("kthSmallestElement is ",kthSmallestElement[k-1])

"""
TC is O(nlogk) if you use heap 
else O(nlogn) in the worst case
"""