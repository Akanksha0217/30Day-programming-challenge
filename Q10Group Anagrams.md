#Group Anagrams:
from collections import defaultdict
def groupAnagrams(strs):
    groups = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(word)
    return list(groups.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
print(groupAnagrams(["abc", "bca", "cab", "xyz", "zyx", "yxz"]))
print(groupAnagrams(["abc", "def", "ghi"]))

