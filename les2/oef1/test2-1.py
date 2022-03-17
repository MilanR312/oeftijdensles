a = int(input("num: "))
while not (500 < a < 1000 and not a % 2):
    a = int(input("fout\nnew number: "))
print(f"correct number = {a}")
