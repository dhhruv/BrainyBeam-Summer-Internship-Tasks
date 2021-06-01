# Dictionary
# : is used to specify the key

data = {1: "pvd", 2: "vsd", 3: "rhd"}
print(data)

# fetching a particular value
print(data[2])

# functions can be used
print(data.get(3))
print(data.get(4, "Not found"))

# dictionary with lists
keys = ["pvd", "vsd", "rhd"]
val = ["c", "php", "c++"]
data = dict(
    zip(keys, val)
)  # dict() function for converting the zipped file into a dictionary
print(data)

# adding an object as key and value
data["avd"] = "js"
print(data)

del data["avd"]  # deleting data
print(data)

# Nested Dictionary
prog = {
    "js": "atom",
    "cs": "vs",
    "python": ["PyCharm", "Sublime", "VC"],
    "java": {"jse": "NetBeans", "jee": "eclipse"},
}
print(prog)
print(prog["js"])
print(prog["python"])
print(prog["python"][0])
print(prog["java"])
print(prog["java"]["jee"])
