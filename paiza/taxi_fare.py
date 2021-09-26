input_line = input()
s = input_line.split(' ')
N = int(s[0])
X = int(s[1])
fare_list = []
for fare in range(N):
    x = input()
    x_ar = x.split(' ')
    fare_list.append(x_ar)
true_fare = []
for test in fare_list:
    if int(test[0]) > X:
        true_fare.append(int(test[1]))
    else:
        f = int(test[0])
        count = 0
        while f <= X:
            f += int(test[2])
            count += 1
        true_fare.append(int(test[1]) + int(test[3]) * count)


print(min(true_fare), max(true_fare))
