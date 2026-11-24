from typing import List

def read_integers() -> List[int]:
    user_input = input()
    user_input = user_input.split(",")
    return [int(numbers) for numbers in user_input]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
