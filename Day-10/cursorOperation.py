with open("Day-10/file.txt",'r') as f:
    print(f.tell())
    print(f.seek(19))
    print(f.read())
    print(f.tell())
    