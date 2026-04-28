
import requests
url="http://httpbin.org/get"
parameter={'name':'Adam', 'age':23}
response=requests.get(url,params=parameter)
print("status:",response.status_code)
data=response.json()
print("response:",data)

