N = 3
S = [1, 2]

room = []
for y in range(1, N + 1):
    if {y} < set(S):
        room.append(1)
    else:
        room.append(0)

print(room)