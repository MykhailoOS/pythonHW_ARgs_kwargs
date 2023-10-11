


# Task2
def simple_check():
    for x in range(1000):
        for y in range(1000):
            check = str(x * y)
            if check == check[::-1]:
                print(f"{check} є паліндромом.\n{check} = {x} * {y}")



fucn1 = simple_check()
print(fucn1)