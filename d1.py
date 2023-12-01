def is_digit_in_string(line_string):
    res = [int(i) for i in line_string if i.isdigit()]
    return res

all = []
with open("input.txt", "r+") as file1:
    for line in file1:
        values = is_digit_in_string(line)
        if len(values) == 1 :
            all.append(values[0] * 11)
        else:
            x = int(str(values[0]) +  str(values[-1]))
            all.append(x)

count = 0
for num in all:
    count += num
print(count)

