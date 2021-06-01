import random

lsn = [1, 2]

le = int(input("Enter Length: "))
lec = -1
le1 = -1
le2 = -1
leo = -1
le3 = -1
le4 = -1

if random.choice(lsn) == 1:
    lec = le // 2
    leo = le - lec
else:
    leo = le // 2
    lec = le - leo

if random.choice(lsn) == 1:
    le1 = lec // 2
    le2 = lec - le1
else:
    le2 = lec // 2
    le1 = lec - le2

if random.choice(lsn) == 1:
    le3 = leo // 2
    le4 = leo - le3
else:
    le4 = leo // 2
    le3 = leo - le4

lsc1 = list("qwertyuiopasdfghjklzxcvbnm") * le1
lsc2 = list("qwertyuiopasdfghjklzxcvbnm".upper()) * le2
lss = list("!\]|[/?.,~`-=\";:><@#$%{}&*()_+'") * le3
lsnu = list("1234567890") * le4

password = (
    random.sample(lsc1, le1)
    + random.sample(lsc2, le2)
    + random.sample(lss, le3)
    + random.sample(lsnu, le4)
)

random.shuffle(password)

print("Password Generated: " + "".join(password))
