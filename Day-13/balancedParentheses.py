def balancedParantheses(paran):
    stack = []
    pair = {'}':'{',']':'[',')':'('}
    for i in paran:
        if i in '({[':
            stack.append(i)
        elif i in '}])':
            if not stack and stack.pop() != pair[i]:
                return 0
    return stack == []
paran = input("Enter the parantheses: ")
if(balancedParantheses(paran)):
    print("Balanced")
else:
    print("Not Balanced")