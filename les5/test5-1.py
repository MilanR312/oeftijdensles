x1 = ord('a')
x2 = ord('z')


for i in range(x1,x2+1):
    print(f"{chr(i)} = {i:>4d}  {chr(i).upper()} = {ord(chr(i).upper())}")
