my_list = [1, 'apple', 3, 'banana', 'cherry', 5]

result = all(map(lambda x: isinstance(x, (int, str)), my_list))

if result:
    print("All elements are integers or strings.")
else:
    print("Not all elements are integers or strings.")