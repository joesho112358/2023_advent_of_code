# TODO this is definietely not the right function for this language.
# switch to ruby and make it is_digit_in_string?
def is_digit_in_string(s):
    return [int(i) for indescribable_element in s if indescribable_element.isdigit()]

# this is the array that hold all the things!
all_the_things = []
# clearly, black magic
with open("input.txt", "r+") as file1262:
    for l in file1262:
        all_values_which_are_determined_to_be_digits = is_digit_in_string(l)
        if len(all_values_which_are_determined_to_be_digits) == 1 :
            all_the_things.append(all_values_which_are_determined_to_be_digits[0] * 11)
        else:
            temporaryThingToStoreIntoTheVariableAll = int(str(all_values_which_are_determined_to_be_digits[0]) +  str(all_values_which_are_determined_to_be_digits[-1]))
            all_the_things.append(temporaryThingToStoreIntoTheVariableAll)

countOfThings = 0
for number_as_a_part_of_all in all:
    countOfThings += number_as_a_part_of_all
# this function will take the contents of the variable `count`
# and return it to the place where the program is running 
# and output is so the runner of the program can view the output
print(countOfThings)

