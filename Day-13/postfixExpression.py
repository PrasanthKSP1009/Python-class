'''
Docstring for Day-13.postfixExpression
1. infix(operators is going to be in between) - whenever the mathematical expression comes it executes
2. prefix(operators is going to be at start) - whenever the mathematical expression comes it executes
3. postfix(operators is going to be in end) - whenever the mathematical expression comes it executes
23*54*+9-
o/p:17
2|3|*54*+9-
6|54*+9-
6|20+9-
26|9-
17
'''
from collections import deque
def postfix(exp):
    stac = deque()
    for i in exp:
        if i.isdigit():
            stac.append(int(i))
        else:
            b = stac.pop()
            a = stac.pop()
            if i == '+':
                stac.append(a+b)
            elif i == '-':
                stac.append(a-b)
            elif i == '*':
                stac.append(a*b)
            elif i == '//':
                stac.append(a//b)
            elif i == '%':
                stac.append(a%b)
    return stac[-1]
exp = '25-3*54*+9-'
print(postfix(exp))
