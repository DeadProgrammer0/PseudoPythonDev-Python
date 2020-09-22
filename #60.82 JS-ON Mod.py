import json

data = '{"var1":"Harry","var2":"54","var3":"True"}'


ab = json.loads(data)
print(ab['var3'])

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
    j.write(json.dumps(x))


with open('dict.json') as f:
    ab1 = json.loads(f.read())
print(ab1)