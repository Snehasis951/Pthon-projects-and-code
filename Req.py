import requests
r = requests.get("https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-81/")
print(r.text)

url = "www.something.com"
data={
    "point_1":5,
    "point_2":10
}
r2 = requests.post(url=url, data=data)