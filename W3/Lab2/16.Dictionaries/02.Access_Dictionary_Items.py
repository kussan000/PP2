#1.Accessing Items

#You can access the items of a dictionary by referring to its key name, inside square brackets:

#Example 1
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"] # Mustang

#There is also a method called get() that will give you the same result:

#Example 2
x = thisdict.get("model")

#2.Get Keys

#The keys() method will return a list of all the keys in the dictionary.

#Example 1
x = thisdict.keys() # dict_keys(['brand', 'model', 'year'])

#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

#Example 1
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#3.Get Values

#The values() method will return a list of all the values in the dictionary.

#Example 1
x = thisdict.values() # dict_values(['Ford', 'Mustang', 1964])

#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.\

#Example 2
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#4.Get Items

#The items() method will return each item in a dictionary, as tuples in a list.

#Example 1
x = thisdict.items() # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

#Example 2
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#5.Check if Key Exists

#To determine if a specified key is present in a dictionary use the in keyword:

#Example 1
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

  