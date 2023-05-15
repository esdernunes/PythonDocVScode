a=10
b=5
op=input("Digite uma operacao:")

if op=="+":
    res=a+b
if op=="-":
    res=a-b
if op=="/":
    res=a/b
if op=="*":
    res=a*b
else:
    print("falso")

print("Operação é " + op + " resposta: = "+str(res)) 
