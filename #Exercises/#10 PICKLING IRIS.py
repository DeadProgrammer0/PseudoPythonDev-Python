
import pickle
import requests

iris_data = requests.get(url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
iris_data_list = iris_data.text.split('\n')

iris_names = requests.get(url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names')
iris_names_list = iris_names.text.split('\n')

with open('irisdata.pkl','wb') as iris_data_file:
    pickle.dump(iris_data_list,iris_data_file)


with open('irisnames.pkl','wb') as iris_names_file:
    pickle.dump(iris_names_list,iris_names_file)


with open("irisdata.pkl","rb") as iris_data_file:
    iris_data_txt = pickle.load(iris_data_file)

with open("irisnames.pkl","rb") as iris_names_file:
    iris_names_txt = pickle.load(iris_names_file)

with open('irisdata.txt','a') as iris_data_file_txt:
    iris_data_file_txt.seek(0)
    iris_data_file_txt.truncate()
    for line in iris_data_txt:
        iris_data_file_txt.write(f'\n{line}')

with open('irisnames.txt','a') as iris_names_file_txt:
    iris_names_file_txt.seek(0)
    iris_names_file_txt.truncate()
    for line in iris_names_txt:
        iris_names_file_txt.write(f'\n{line}')

