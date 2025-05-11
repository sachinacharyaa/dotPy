# A Python dictionary is a data structure that
# stores the value in key: value pairs.


# create dictionary using { }
d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print(d1)                   # {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# create dictionary using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)                    # {'a': 'Geeks', 'b': 'for', 'c': 'Geeks'}




# Accessing Dictionary Items
# We can access a value from a dictionary by
# using the key within square brackets orget()method.


d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])              #Alice  

# Access using get()
print(d.get("name"))          #Alice





#Adding and Updating Dictionary Items

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"

print(d) 
         #{1: 'Python dict', 2: 'For', 3: 'Geeks', 'age': 22}