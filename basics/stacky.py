stack = []
stack.append('A')
stack.append('B')
stack.append('C')
print("Current Stack : ", stack)

print(stack[1])
print(stack[2])
print(stack[0])

top_element = stack[-1]
print('Peeking at the top element : ', top_element)

popped_element = stack.pop()
print("Popped Element : ", popped_element)
print("Stack after the popped element : ", stack)

is_empty = len(stack) == 0
print("Is stack empty? ", is_empty)

stack.pop()
stack.pop()

is_empty = len(stack) == 0
print("Is stack empty? ", is_empty)