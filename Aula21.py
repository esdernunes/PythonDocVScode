valores=[1,5,6,6,10]

def soma(num):
    r=0
    for m in num:
        r+=m
    return(r)
    


def sub(num):
    r=0
    for m in num:
        r-=m
    return(r)

print(valores,"A soma é: ",soma(valores))

print(valores,"A subtração é: ",sub(valores))