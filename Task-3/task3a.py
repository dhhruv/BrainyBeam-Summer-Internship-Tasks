import random as r

print(
    "Random Float:  ", r.random()
)  # it will return random float value between 0.0 & 1.0

print(
    "Random Integer:  ", r.randint(50, 150)
)  # it will print random integer value between specified integers

print(
    "Random Range:  ", r.randrange(11, 111, 11)
)  # it will return an element randomly and it contains arguments (start,stop,step)

print(
    "Random Choice:  ", r.choice("element to be selected from here")
)  # it will choose an element from specified string or variable

a = ["s", "h", "u", "f", "f", "l", "e"]
r.shuffle(a)
print("Random Shuffle:  ", a)  # it will shuffle the given list
