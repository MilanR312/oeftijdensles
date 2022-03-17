import time

start = time.time()
for i in range(1000):
    print((lambda x: ("kort", "middel", "lang")[x // 500])(i))
time1 = time.time() - start
start = time.time()
for i in range(1000):
    woord = str(i)
    if len(woord) <= 5:
        print("Dit is een kort woord")
    elif len(woord) > 5 and len(woord) <= 10:
        print("Dit is een middellang woord")
    else:
        print("Dit is een lang woord")
time2 = time.time() - start

print(time1)
print(time2)
