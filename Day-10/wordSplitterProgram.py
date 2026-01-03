with open("Day-10/file.txt",'r') as f:
    words = f.read()
    words = words.split()
    print(len(words))
    for word in words:
        print(word)