from collections import Counter

a = Counter("encyclopedia")
print(a)
print(a.most_common(3))
print(a.clear())
print(a.most_common(3))