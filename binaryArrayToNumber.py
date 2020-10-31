def binary_array_to_number(arr):
    total = []
    for index,data in enumerate(arr):
        if(data == 1):
            total.append(2**(len(arr) - (index+ 1)))
    return sum(total)