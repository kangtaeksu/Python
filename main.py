A, B = input().split()

_min = len(A)
for i in range(len(B)-len(A)+1):# b를 a의 곳곳에 대입해본다2개차이나면 3번가능
    count = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:#다를 때마다 카운트새고
            count += 1
    if count < _min:# 에이글자수보다 작을때
        _min = count #반복할때마다 갱신하기위해서 (최소로)

print(_min)