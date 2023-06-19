# sample code to implement a stack using list

stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print('initial stack')
print(stack)

# pop()
print('/nElements popped from the stack:')
print(stack.pop()) #'c'
print(stack.pop()) #'b'
print(stack.pop()) #'a'
print(stack) #empty list