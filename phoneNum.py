import sys
input = sys.stdin.readline
i =1
while True:
    l, p, v = map(int, input().split())
    if l+ p +v ==0:
        break
    result = l*(v//p)
    result+=min((v%p),l)
    print('Case %d: %d' %(i, result))
    i+=1