## Пока работает на SQLite

Запустить проект:
```
make apprun
```
### Если что-то пойдет не так - дополнительные команды

Выполняем миграции:
```
python manage.py migrate
```
Создаем пользователя:
```
python manage.py createsuperuser
```
Заполняем базу:
```
python manage.py fill_db_fake
```
Запускаем сервер:
```
python manage.py runserver
```