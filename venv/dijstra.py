import heapq
graph=[[] for i in range (node)]
graph[a].append((b, cost))

def dij(start):
    q= []
    heapq.heappush(q, (0, start))
    distance[start] =0
    while q:
        dist, now=  heapq.pop(q)
        if distance[now]< dist:
            continue
        for i in graph[now]:
            cost = dist+ i[1]
            if cost< distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
