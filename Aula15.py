t_carros=("HRV","Golf","Argo","focus")

l_carros=list(t_carros)
l_carros[2]="ka"
t_carros=tuple(l_carros)


for x in l_carros:
    print(x)