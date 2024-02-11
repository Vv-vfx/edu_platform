import requests
from requests.auth import HTTPBasicAuth

url = "http://127.0.0.1:8000/api/course/"

username = 'student'
password = '12345'
token = '638170ddef243f691155deaa025b6f8c81e3de9e'

# первый вариант с базовой аутентификацией
response = requests.get(url, auth=HTTPBasicAuth(username, password))
assert response.status_code == 200, response.status_code
print(response.json())

# второй вариант с токеном
headers = {'Authorization': f'Token {token}'}
response = requests.get(url, headers=headers)
assert response.status_code == 200, response.status_code
print(response.json())

# ====================================
# третий вариант с токеном
# с группами

# username = 'curator'
# password = '12345'
token = 'd050fab02160e9d5d8a5b9610214fe5a9c6ff64b'

headers = {'Authorization': f'Token {token}'}
response = requests.get(url, headers=headers)
assert response.status_code == 200, response.status_code
print(response.json())


# четвертый вариант с токеном
# с группами

# username = 'curator'
# password = '12345'
token = 'd050fab02160e9d5d8a5b9610214fe5a9c6ff64b'

headers = {'Authorization': f'Token {token}'}
response = requests.get(url, headers=headers)
assert response.status_code == 200, response.status_code
print(response.json())

# пятый вариант с токеном
# с группами

# username = 'curator'
# password = '12345'
token = 'd050fab02160e9d5d8a5b9610214fe5a9c6ff64b'

# Данные курса
course_data = {
    'name': 'Новый курс по Джанго',
    'description': 'Описание курса',
    'price': 9999,
    # 'category': '1'

    # Другие поля, требуемые API
}


headers = {'Authorization': f'Token {token}'}
response = requests.post(url, headers=headers, json=course_data)
assert response.status_code == 201, response.status_code
print(response.json())