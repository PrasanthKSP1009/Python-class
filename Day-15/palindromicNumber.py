'''
Docstring for Day-15.palindromicNumber
'''
def reverseNum(num):
    if (num == 0):
        return 0
    rev = 0
    while num:
        rev = (rev*10) + (num% 10)
        num //= 10
    return rev
def isPalindrome(x):
    if (x < 0):
        return False
    num = reverseNum(x)
    print(x,num)
    return x == num