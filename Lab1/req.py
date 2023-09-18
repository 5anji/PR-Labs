import requests

data = requests.post("http://localhost:5000/hello", "{\"smth\" : \"123\"}")



print(data.json())
