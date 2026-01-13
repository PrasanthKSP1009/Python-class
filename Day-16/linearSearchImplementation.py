'''
lis = list(map(int,input().split()))
target = int(input())
for ele in lis:
    if ele == target:
        print("Element Found")
        exit(0)
print("Hi")# It will not execute due to exit(0)
'''
def linearSearch(elements,target):
    for ele in elements:
        if ele == target:
            return "Element Found"
            exit(0)
lis = list(map(int,input().split()))
target = int(input())
print(linearSearch(lis,1))
print(linearSearch(lis,5))