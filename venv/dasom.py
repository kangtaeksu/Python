participant =["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

participant.sort()
completion.sort()
for a, b in zip(participant, completion):
    if a!=b:
        print(a)
        break
    print(a)
    print(b)