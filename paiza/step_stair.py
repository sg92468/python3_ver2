N = int(input())
inp = input().split(' ')
A = int(inp[0])
B = int(inp[1])
N_steps = list(range(1, N + 1))
A_step = 0
A_count = 0
while A_step < N:
    A_step += A
    A_count += 1
B_step = 0
B_count = 0
while B_step < N:
    B_step += B
    B_count += 1
AB_count = [A_count, B_count]
pattern = AB_count[1]
for n in range(pattern):
    steps = []
    total_step = 0
    for x in range(n):
        total_step += B
        steps.append(total_step)
    while total_step < N:
        total_step += A
        steps.append(total_step)
    if total_step > N:
        steps.append(N)
    for y in range(len(steps)):
        if steps[y] in N_steps:
            N_steps.remove(steps[y])
print(len(N_steps))
