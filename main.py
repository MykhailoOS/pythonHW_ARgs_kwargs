# def parser(numbers: str) -> list:
#     return list(map(int, numbers))
#
#
# def is_arithmetic_sequence(numbers: list) -> bool:
#     if numbers[1] - numbers[0] == numbers[4] - numbers[3]:
#         return True
#     return False
#
#
#
# def is_geometric_sequence(numbers: list) -> bool:
#     if numbers[1] / numbers[0] == numbers[4] / numbers[3]:
#         return True
#     return False
#
#
# def next_arithmetic_item(numbers: list) -> int:
#
#     minus = numbers[1] - numbers[0]
#     numbers.append(numbers[1] + minus)
#
#
# def next_geometric_item(numbers: list) -> int:
#     devision = numbers[1] / numbers[0]
#     numbers.append(numbers[1] * devision)
#
# def get_next_item(numbers: list):
#     if len(numbers) > 2:
#         if is_arithmetic_sequence(numbers):
#             return next_arithmetic_item(numbers)
#
#         if is_geometric_sequence(numbers):
#             return next_geometric_item(numbers)
#
#     return None
#
#
# if __name__ == '__main__':
#     numbers = input('numbers>>>')
#     numbers = parser(numbers)
#     print(get_next_item(numbers))


#Task2
# def simple_check():
#     for x in range(1000):
#         for y in range(1000):
#             check = str(x * y)
#             if check == check[::-1]:
#                 print(f"{check} є паліндромом.\n{check} = {x} * {y}")
#
#
#
# fucn1 = simple_check()
# print(fucn1)