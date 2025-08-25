#Permutations of a String

def permuteUnique(s: str):
    res = []
    chars = sorted(s)
    used = [False] * len(chars)
    def backtrack(path):
        if len(path) == len(chars):
            res.append("".join(path))
            return
        for i in range(len(chars)):
            # skip used chars
            if used[i]:
                continue
            # skip duplicates (when the previous char is the same and not used)
            if i > 0 and chars[i] == chars[i-1] and not used[i-1]:
                continue
            used[i] = True
            path.append(chars[i])
            backtrack(path)
            path.pop()
            used[i] = False
    backtrack([])
    return res

print(permuteUnique("abc"))
print(permuteUnique("aab"))
print(permuteUnique("aaa"))
print(permuteUnique("a"))
print(len(permuteUnique("abcd")))

