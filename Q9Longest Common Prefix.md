#Longest Common Prefix
#You are given an array of strings strs[], consisting of lowercase letters. Your task is to find the longest common prefix shared among all the strings. If there is no common prefix, return an empty string "".A common prefix is a substring that appears at the beginning of all the strings in the array. The task is to identify the longest such prefix that all strings share.


def longestCommonPrefix(strs):
    if not strs: 
        return ""
    prefix = strs[0] 
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]  
            if not prefix:
                return ""
    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))  
print(longestCommonPrefix(["dog", "racecar", "car"]))    
print(longestCommonPrefix(["interspecies", "interstellar", "interstate"]))  
print(longestCommonPrefix(["a"]))                         
print(longestCommonPrefix([]))                            


