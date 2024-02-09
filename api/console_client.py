import requests
from requests.auth import HTTPBasicAuth

url = "http://127.0.0.1:8000/api/course/"

username = 'Ivan'
password = 'xxxccc3456567'
token = '82691fa59bf07bb6831818583e56622be251dbd3'

# первый вариант с базовой аутентификацией
# # response = requests.get(url, auth=HTTPBasicAuth(username, password))
# response = requests.get(url, auth=HTTPBasicAuth(username, password))
# assert response.status_code == 200, response.status_code
# print(response.json())

# второй вариант с токеном
headers = {'Authorization': f'Token {token}'}
response = requests.get(url, headers=headers)
assert response.status_code == 200, response.status_code
print(response.json())






