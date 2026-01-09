def revString(rev):
    if (len(rev) <= 1):
        return rev
    return revString(rev[1:])+rev[0]
string = input("Enter a String: ")
reversedString = revString(string)
print(string,reversedString)