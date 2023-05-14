numbers = [1,1,2,3,5,8,13,21,34,55]

squared = [(num * num) for num in numbers]
print(squared)

even_numbers = [num for num in numbers if (num % 2 == 0)]
print(even_numbers)

with open('file1.txt', 'r') as file1:
    first = file1.readlines()
    first_list = [int(n) for n in first]
    print(first_list)

with open('file2.txt', 'r') as file2:
    second = file2.readlines()
    second_list = [int(m) for m in second]
    print(second_list)

common_list = [i for i in first_list for j in second_list if i == j]
print(common_list)