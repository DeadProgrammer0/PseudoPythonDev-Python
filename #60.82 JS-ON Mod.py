import json

data = '{"var1":"Harry","var2":"54","var3":"True"}'


ab = json.loads(data)


x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
]

}

with open('jsontest.json','w') as j:
    j.write(json.dumps(data))


with open('dict.json') as f:
    ab1 = json.loads(f.read())
print(ab1)

with open('jsontest2.json','w') as f:
    json.dump(x,f,indent=True)

with open('jsontest2.json','r') as f:
    ab2 = json.load(f)
print(ab2)