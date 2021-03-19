
collected = []
number ="1231234"
k =3
for (i, num) in enumerate(number):
    print(i, num)
        # collected에 원소가 있고 마지막원소가 지금넣은놈보다 작고, k 가 0보다 클때 순회
    while collected and collected[-1] < num and k > 0:

        collected.pop()
        k -= 1

    if k == 0:
        collected += number[i:]
        break

    collected.append(num)

collected = collected[:-k] if k > 0 else collected

answer = "".join(collected)


