def add_two_numbers() -> int:
    user_input = input()
    user_input = user_input.split(",")
    number_list = [int(num) for num in user_input]
    return sum(number_list)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
