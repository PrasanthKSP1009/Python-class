setEg1 = set() #{},{1,2,3}
setEg1.add(1)
setEg1.add(5)
setEg1.add(5)
setEg1.add(6)
print(setEg1)
setEg2 = {1,7}
set3 = setEg2 | setEg1
print(set3)
set4 = setEg2 & setEg1
print(set4)
set5 = setEg1 - setEg2
print(set5)
set6 = setEg2 - setEg1
print(set6)