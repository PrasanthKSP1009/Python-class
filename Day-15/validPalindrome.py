'''
Docstring for Day-15.validPalindrome
'''
def isPalindrome(s):
    string = ""
    for i in s:
        char = i.lower()
        if char.isalnum():
            string+=char
    return string == string[::-1]