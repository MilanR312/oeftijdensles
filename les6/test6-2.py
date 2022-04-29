a = getattr(int,dir(int)[32])(int,6)
b = getattr(int,dir(int)[32])(int,4)
s = getattr(int,dir(int)[59])(a,b)
o = getattr(float,dir(int)[62])(s)
print(o)

o = float.as_integer_ratio(1/10)
print(o)