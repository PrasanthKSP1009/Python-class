def reverse(str):
    revStr = ""
    stack = []
    for i in str:
        stack.append(i)
    while stack:
        revStr += stack.pop()
    return revStr

str = input("Enter the String: ")
print("Reversed String is", reverse(str))
