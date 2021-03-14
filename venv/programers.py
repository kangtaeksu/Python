from collections import Counter  # 요소마다의 개수새는데 활용
from functools import reduce
clothes =[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

cnt = Counter([kind for name, kind in clothes])
answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
print(cnt)