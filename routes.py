import requests

BASE="http://127.0.0.1:5000/"

data = [{"name":"Hello", "likes":10, "views":100},
        {"name":"World", "likes":3, "views":0},
        {"name":"!", "likes":52, "views":321}]

for i, d in enumerate(data):
    response = requests.put(BASE + "video/" + str(i), d)
    print(response.json())


response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/3")
print(response.json())
