from collections import deque

# FIFO - First In First Out
# peoples standing in queue in-front of restaurant
# add items in queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# popping the items in queue
queue.popleft()
print(queue)

queue.clear()
if not queue:
    print("queue is empty")
