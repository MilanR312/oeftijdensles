def ggd(a,b):
    x = max(a,b)
    y = min(a,b)
    R = x%y
    while R != 0:
        x = y
        y = R
        R = x%y
    return y

def zn_ond_ondel(a,b):
    if ggd(a,b) == 1:
        return True
    else:
        return False

def prnt_ond(a,b):
    for i in range(a,b):
        for j in range(a,b):
            if not zn_ond_ondel(i,j):
                print((i,j), end=" ")
prnt_ond(2,50)