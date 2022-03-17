import string
while True:
    num = [0,0,0]
    password = input()
    if 6 < len(password) < 20:
        for let in password:
            if let in string.ascii_letters:
                num[0] = 1
            if let in string.digits:
                num[1] = 1
            if let in string.punctuation:
                num[2] = 1

            if sum(num) > 2:
                print("ok")
                print(password)
                break
        else:
            continue
        break
    print("niet ok")