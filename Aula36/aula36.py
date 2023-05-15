import json

carros={"marca":"honda",
        "modelo":"Civic",
        "cor":"preto"
        }

carros_json=json.dumps(carros)

print(carros_json)

for x,v in carros.items():
    print(x,v)