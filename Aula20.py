
# `def` is a keyword in Python used to define a function. In the given code, `def somar(n1,n2):`
# defines a function named `somar` that takes two arguments `n1` and `n2` and adds them together to
# produce the result.
def somar(n1,n2,n3,n4):
    res=n1+n2+n3+n4
    print(res)
    
def textos(*p):
   for t in p:
    print(t)


textos("Aula","curso","python")    

somar(5,7,5,5)
somar(12,8,4,6)
somar(1,20,47,4)


def carros(c):
    print("Modelo: " + c)

carros("celta")


valores=[1,5,6,6,5]

def sub(num):
    r=0
    for m in num:
        r+=m
    print("Soma: " , r)
    

sub(valores)






