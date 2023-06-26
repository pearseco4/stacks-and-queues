# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# SOLUTION  
class Solution: 
    def isValid(self, s: str) -> bool:
      stack = []
    #   hash map. Take every closing parentheses and map it to an open parentheses.  
      closeToOpen = { ")": "(", "}": "{", "]": "["}

      #   going through every character (c) in the input string (s)
      for c in s: 
        if c in closeToOpen:
            # stack[-1] is the last value added to the stack
            if stack and stack[-1] == closeToOpen[c]:
              stack.pop()
            else: 
              return False
        else: 
           stack.append(c)
      return True if not stack else False