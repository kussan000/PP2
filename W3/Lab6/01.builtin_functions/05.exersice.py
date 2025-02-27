def check_true(string):
    list1 =list(map(int,string.split()))
    return all(list1)

s = input("Enter  your list: ")
print("All of your list is", check_true(s))