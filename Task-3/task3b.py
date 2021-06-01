import random as r
import string as s

try:
    n = int(input("Enter the length of desired password: "))
    if n < 8 or n > 16:
        raise Exception("Length of a password must be between 8 to 16...")
    p1 = "".join(r.choice(s.ascii_letters) for x in range(n - 2))
    p2 = "".join(r.choice(s.digits) for x in range(1, n - 1))
    p3 = "".join(r.choice(s.punctuation) for x in range(1, n - 1))
    pws1 = "".join(p1 + p2 + p3)
    pws2, ss = [], []
    pws2[:0] = pws1
    r.shuffle(pws2)
    for i in range(n):
        ss.append(pws2[i])
    p = "".join(ss)
    print("Your password is: {}".format(p))
except Exception as e:
    print(e)
