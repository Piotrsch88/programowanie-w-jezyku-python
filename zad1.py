#lista imion
def print_names(names):
    for name in names:
        print(name)

print_names( ["tomasz", "arkadiusz", "mateusz", "damian", "stanisław"])

#lista liczb przemnożonych przez 2 pętla for
def multiply_numbers_by_two(numbers):
    numbers_multiplied_by_two = []

    for number in numbers:
        number_multiplied_by_two = number * 2
        numbers_multiplied_by_two.append(number_multiplied_by_two)

    return numbers_multiplied_by_two

print(multiply_numbers_by_two([1,2,3,4,5]))

#lista liczb przemnożonych przez 2 lista składana
def multiply_numbers_by_two_using_list_comprehension(numbers):
    return [number * 2 for number in numbers]

print (multiply_numbers_by_two_using_list_comprehension([1,2,3,4,5]))


# # lista 10 cyfr wyświetla liczby parzyste
# numbers1 = [1,2,3,4,5,6,7,8,9,10]
# for numbers1 in range (1,11):
#     print(numbers1)
# for numbers1 in range (1,11):
#     if numbers1 % 2 == 0:
#         print(numbers1)
#
# # #lista 10 cyfr wyświetla co drugi element
# numbers2 = [11, 12, 13, 14, 15,16, 17, 18, 19,20]
# for numbers2 in range (11,21):
#     print (numbers2)
# for numbers2 in range (11,21):
#     if numbers2 % 2 == 0:
#         print(numbers2)








