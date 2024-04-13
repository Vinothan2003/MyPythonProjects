stack = []
# LIFO --> Last In First Out
# real world example for stack is the note or plate in order
# add in items to the stack
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# popping items in the stack
last = stack.pop()
print(f"the item {last} is popped ")
print(stack)

# clearing the stack
stack.clear()
print(stack)

if not stack:
    print("the stack is empty")
