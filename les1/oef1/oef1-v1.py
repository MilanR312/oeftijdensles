word = input()
print((lambda x: ("kort", "middel", "lang")[x // 500])(word))
