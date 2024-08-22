"""
User enters string of numbers dividing by space. Script returns minimal number
Input:
1 2 3 4 5

Output:
1
"""
from typing import List


def get_user_input() -> str:
    """
    returning user input without transformation
    :return:
    """
    user_input = input("Enter numbers dividing by space: ").strip()
    return user_input


def valid_user_input(user_input: str) -> List[int]:
    """
    Converting user input to list of int
    :param user_input: raw user input
    :return: transforming list of int
    """
    valid_list = []

    for num in user_input.split():
        valid_list.append(int(num))

    return valid_list


def make_min(valid_list: List[int]) -> int:
    """
    Getting list of int and returning minimal digit of this list
    :param valid_list: list of int
    :return: minimal digit
    """
    min_value = min(valid_list)

    return min_value


def main():
    user_input = get_user_input()
    print("user_input: ", user_input)
    valid_list = valid_user_input(user_input)
    result = make_min(valid_list)
    print("result =", result)


if __name__ == '__main__':
    main()
