# pickle
# Use requests module to download the iris dataset

import requests
import pickle

x = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
print(x)

# list_1 = x.split("\n")
# print(list_1)

list_2 =[item.split(",") for item in x.split("\n") if len(item)!=0]
print(list_2)

with open("myiris.pkl", "wb") as s:
    pickle.dump(list_2, s)