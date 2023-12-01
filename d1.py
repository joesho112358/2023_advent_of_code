# Program to show various ways to
# read data from a file.





def is_digit_in_string(line_string):
    

    # printing original string 
    print("The original string : " + line_string)

    # using List comprehension + isdigit() +split()
    # getting numbers from string 
    res = [int(i) for i in line_string if i.isdigit()]

    # print result
    return res

print('here')
all = []
with open("input.txt", "r+") as file1:
	# Reading from a fil
    print('here')

    for line in file1:
        print('line')
        values = is_digit_in_string(line)
        if len(values) == 1 :
            all.append(values[0] * 11)
        else:
            x = int(str(values[0]) +  str(values[-1]))
            all.append(x)

print('alll')
print(all)
cout = 0
for num in all:
    cout += num
print(cout)
