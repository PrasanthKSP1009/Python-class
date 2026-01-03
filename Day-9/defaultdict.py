from collections import defaultdict
'''
a = defaultdict(list)
words = ["cat","apple","rat","orange","dog","banana"]
for word in words:
    a[len(word)].append(word)
print(list(a.values()))
'''
grp_ana = defaultdict(list)
words = ["eat","tea","tan","ate","nat","bat"]
for word in words:
    key = ''.join(sorted(word))
    grp_ana[key].append(word)
print(list(grp_ana.values()))