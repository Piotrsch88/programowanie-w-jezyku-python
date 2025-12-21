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


# lista 10 cyfr wyświetla liczby parzyste

def even_numbers(numbers1):
    for number1 in numbers1:
        if number1 % 2 ==0:
            print(number1)
even_numbers(list(range(1,11)))



#lista 10 cyfr wyświetla co drugi element

def every_other_element(numbers2):
    for i in range(1, len(numbers2), 2):
        print(numbers2[i])
every_other_element(list(range(13,23)))











