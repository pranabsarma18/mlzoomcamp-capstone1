import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url': 'https://i.postimg.cc/3w7R5jtK/Corn-Blight-148.jpg'}

result = requests.post(url, json=data).json()
print(result)