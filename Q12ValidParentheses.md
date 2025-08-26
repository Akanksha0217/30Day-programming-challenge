#Valid Parentheses with Multiple Types

def isValid(s: str) -> bool:
    prev = None
    while s != prev:  # keep removing until stable
        prev = s
        s = s.replace("()", "").replace("{}", "").replace("[]", "")
    return s == ""

print(isValid("()"))  
print(isValid("([)]"))  
print(isValid("[{()}]"))  
print(isValid(""))          
print(isValid("{[}"))       
print(isValid("((){})"))  
