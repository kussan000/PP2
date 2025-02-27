from functools import reduce

def mult(list_func):
    my_list=list(map(int,list_func.split()))

    result = reduce(lambda x, y: x * y, my_list)

    return result

list1 = input("Enter your numbers: ")

print(mult(list1))