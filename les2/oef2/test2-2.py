import random as rn

a = rn.randint(2, 20)
x = int(input("geuss "))


def hoglag(a, b):
    return "lager" if b < a else "groter"


tries = 4
while x != a and tries > 0:
    x = int(input(f"fout het getal is {hoglag(x,a)}, {tries} remaining:\nnew number:"))
    tries -= 1
print("juist") if x == a else print("fout")
