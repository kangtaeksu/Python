n = int(input())
order =[]
for i in range(n):
    command = input().split()
    if command[0]  == "pop":
        order.pop()
    if command[0]  == "size":
        print(len(order))
    if command[0]  == "empty":
        if len(order)==0:
            print(1)
        else:
            print(0)
    if command[0]  == "top":
        order.pop(0)
    if command[0] == "push" :
        order.append(command[1])