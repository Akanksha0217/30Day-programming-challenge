def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s
    start, max_len = 0, 1
    def expandAroundCenter(left: int, right: int):
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start, max_len = left, right - left + 1
            left -= 1
            right += 1
    for i in range(len(s)):
        # Odd length palindrome
        expandAroundCenter(i, i)
        # Even length palindrome
        expandAroundCenter(i, i + 1)
    return s[start:start + max_len]

print(longestPalindrome("babad"))  
print(longestPalindrome("cbbd"))   
print(longestPalindrome("a"))      
print(longestPalindrome("aaaa"))  
print(longestPalindrome("abc"))    
