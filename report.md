### Задание №1

Проверка версии python:

`python --version`

Обновление зависимостей:

`pip freeze > requirements.txt`

Файлы задания:

```
cache.py
main.py
```

Проверка задания:

`python main.py`

### Задание №2

Проверка установки:

```
nginx -v
wrk --version
gunicorn --version
```

Папка для статики: public/

Запуск gunicorn:

`gunicorn password_app:app --bind 127.0.0.1:8000 --workers 4`

Запустить nginx со своим конфигом:
```
nginx -t -p "$PWD" -c nginx.conf
nginx -p "$PWD" -c nginx.conf
```
Остановка:
`nginx -p "$PWD" -c nginx.conf -s stop`

Проверка статики:
открыть `http://127.0.0.1:8080/public/имя_файла`

Проверка проксирования через nginx: открыть `http://127.0.0.1:8080/gunicorn/` или `http://127.0.0.1:8080/gunicorn/?length=16`

Проверка напрямую WSGI: открыть `http://127.0.0.1:8000/` или `http://127.0.0.1:8000/?length=10`

Сделать 3 замера производительности:

    wrk -t8 -c700 -d20s http://127.0.0.1:8080/public/image.png

    wrk -t8 -c780 -d15s http://127.0.0.1:8080/gunicorn/

    wrk -t8 -c130 -d15s http://127.0.0.1:8000/


Ошибки начинают выводиться при:
    
    wrk -t8 -c770 -d20s http://127.0.0.1:8080/public/image.png

    wrk -t8 -c790 -d15s http://127.0.0.1:8080/gunicorn/

     wrk -t8 -c140 -d15s http://127.0.0.1:8000/

### Задание №3

Запуск Django через gunicorn:

`gunicorn book_catalog.wsgi:application --bind 127.0.0.1:8000 --workers 4`

Запуск nginx:

    nginx -t -p "$PWD" -c nginx.conf
    nginx -p "$PWD" -c nginx.conf