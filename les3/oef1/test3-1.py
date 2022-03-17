inp = input()
out = ''.join([i for i in inp if i.lower() not in "aeiou"])
print(out)