from collections import deque
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
dx= [0,0,1,-1]
dy= [1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    while queue:#큐가 빌떄까지
        x,y = queue.popleft() #좌표하나씩뺴면서
        for i in range(4):#4방향확인
            nx= x+ dx[i]
            ny= y+ dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:#범위밖제외
                continue
            if graph[nx][ny] == 0:#상하좌우움직엿는데 0인곳(못감)이면 무시
                continue
            #여기가 중요 해당노드를 처음 방문하는 경우에만 최단경로
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                #예를듦ㄴ (0,0)에서 1이엿는데 한칸갓으니까 (0,1)은 2로 카운트
                queue.append((nx,ny))#그리고 본인은 2가되면서 주변봐서 또 첨보는 즉, 1이면 1더해줌-> 3이됨이런식으로 최단경로획득
    return graph[n-1][m-1]

print(bfs(0,0))

