import json

carros_dictionary={"marca":"honda",      
        "modelo":"Civic",
        "cor":"preto"
        }                    #dictionary  ->  objeto json

carros_list=["ferrari","audi","lamborghini","ford","madza"]   #list ->  array json

carros_tupla=("ferrari","audi","lamborghini","ford","madza")   #tupla ->  array json

carros_j=json.dumps(carros_dictionary,indent=0,separators=(":","="),sort_keys=True)


print(carros_j)

