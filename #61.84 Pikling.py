# Pickle Module

import pickle
from pickle import load


cars = [{"Rolls-Royce":"Phantom"},{"Bentley":"Flying Spur"},{"Mercedes":"Maybach S650"},{"Bentley":"Mulsanne"},{"Range Rover":"SVAutobiography"}]

with open("cars.pkl","wb") as file:
    pickle.dump(cars,file)

with open("cars.pkl","rb") as file:
    cars2 = pickle.load(file)

# print(cars2)


dummy = pickle.dumps(cars)
loader = pickle.loads(dummy)

for i in loader:
    i = {v:k for k,v in i.items()}
    for k,v in i.items():
        if v == 'Bentley':
            print(i)