'''
Docstring for Day-13.paranthesesQuestion
() - Vaild
( - InValid
) - InValid
((()))) - InValid
((())) - Valid
Counting Logic
'''
def isValid(paran):
    count = 0
    for i in paran:
        if i == '(':#({[
            count += 1
        elif i == ')':#}}}
            count -= 1
        if count < 0:
            return 0
    return count == 0
paran = input("Enter the parentheses: ")
if(isValid(paran)):
    print("Valid")
else:
    print("Invalid")