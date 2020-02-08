def make_list(endpoint, increment):
    numbers = []
    for i in range(0, endpoint, increment):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

make_list(10,2)
