def low(string):
    lower_count = len(list(filter(str.islower, string)))

    return lower_count

def up(string):
    upper_count = len(list(filter(str.isupper, string)))

    return upper_count

s = input("Enter your srting: ")

print("Count of lower letters is", low(s))
print("Count of upper letters is", up(s))