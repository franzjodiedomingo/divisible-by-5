# Print numbers from a list that are divisible by 5
# Make a list

def display_divisible_by_5(my_list):
    divisible_numbers = [num for num in my_list if num % 5 == 0]
    print("Divisible by 5:", divisible_numbers)

my_list = 10, 20, 33, 46, 55
print ("Given list is:", my_list)
display_divisible_by_5(my_list)
