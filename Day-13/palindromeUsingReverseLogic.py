string = input("Enter a string: ")
revStr = ""
stack = []
for i in string:
    stack.append(i)
while stack:
    revStr+=stack.pop()
print(string, revStr)
if(string == revStr):
    print("Given String is Palindrome")
else:
    print("Given String is not a Palindrome")

#One Liner Palindrome checker
print("Palindrome" if (str == str[::-1]) else "Not Palindrome")