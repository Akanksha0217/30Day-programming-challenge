def insert_sorted(stack, element):
    # Base case: place element if stack is empty or top <= element
    if not stack or stack[-1] <= element:
        stack.append(element)
        return
    # Remove top and recurse
    temp = stack.pop()
    insert_sorted(stack, element)
    stack.append(temp)
    
def sort_stack(stack):
    # Base case: empty stack
    if not stack:
        return   
    # Remove top
    temp = stack.pop()   
    # Sort the remaining stack
    sort_stack(stack)  
    # Insert the popped element back in sorted order
    insert_sorted(stack, temp)  
    return stack

print(sort_stack([3, 1, 4, 2]))      
print(sort_stack([7, 1, 5]))         
print(sort_stack([5]))              
print(sort_stack([-3, 14, 8, 2]))   
print(sort_stack([]))               
print(sort_stack([3, 3, 3]))         

