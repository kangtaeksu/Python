def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j ==0: #삼각형 젤왼쪽
                triangle[i][j] +=triangle[i-1][j]
            elif j==i: #삼각형젤오른쪽라인
                triangle[i][j] +=triangle[i-1][j-1]
            else:
                triangle[i][j] +=max(triangle[i-1][j-1], triangle[i-1][j])
        return  max(triangle[-1])#마지막줄에서 가장큰값이므로 -1