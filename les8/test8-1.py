def tel_tekens(filelocation):
    with open(filelocation) as f:
        filecontent = f.read()
        chars = set(filecontent)
        letterfreq = {}
        for char in chars:
            b = filecontent.count(char)
            letterfreq[char] = b
    letterfreq = dict(sorted(letterfreq.items(), key=lambda x: x[1], reverse=True))
    return letterfreq
li = tel_tekens("test.txt")
print(li)