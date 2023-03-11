input_data = list(map(int, input()))

input_data.sort(reverse=True)
for i in range(len(input_data)):
    print(input_data[i], end='')
