with open("Day-10/merge1.txt",'r') as f1, open("Day-10/merge2.txt",'r') as f2:
    text = f1.read() + '\n' + f2.read()
with open("Day-10/mergedText.txt",'w') as f:
    f.write(text)