from collections import deque

dq = deque([1, 2, 3])

# Append elements
dq.append(4)         # deque becomes: [1, 2, 3, 4]
dq.appendleft(0)     # deque becomes: [0, 1, 2, 3, 4]

# Pop elements
dq.pop()             # deque becomes: [0, 1, 2, 3]
dq.popleft()         # deque becomes: [1, 2, 3]

# Extend deque
dq.extend([5, 6])    # deque becomes: [1, 2, 3, 5, 6]
dq.extendleft([0])   # deque becomes: [0, 1, 2, 3, 5, 6]

# Rotate deque
dq.rotate(1)         # deque becomes: [6, 0, 1, 2, 3, 5]
dq.rotate(-1)        # deque becomes: [0, 1, 2, 3, 5, 6]

# Count occurrences
print(dq.count(1))   # Output: 1

# Remove an element
dq.remove(1)         # deque becomes: [0, 2, 3, 5, 6]
