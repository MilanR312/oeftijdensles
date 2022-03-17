word = input()
print((lambda x: ("kort", "middel", "lang")[x // 5])(len(word)))
