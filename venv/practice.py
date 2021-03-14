answer = 0
from collections import deque
priorities=[2, 1, 3, 2]
location =2

d = deque([(v, i) for i, v in enumerate(priorities)])
print(d)
while len(d):
    item = d.popleft()
    print(item)
    if d and max(d)[0] > item[0]:
        d.append(item)
    else:
        answer += 1
        if item[1] == location:
            break
print(answer)