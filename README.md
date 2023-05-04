**Для запуска проекта есть 2 способа:**
- Через докер
- Локально

Перед запуском необходимо создать `.env` файл и поместить в него код проекта:
```
SECRET_KEY=django-insecure-@^r85c*ux#d%g9&hg!w1h5zlph=ia=h9*s_^&k4qyvc%wps7%7
```

Так же, для аутентификации с помощью JWT токена, необходимо раскомментировать строки 151-153 в `settings`:
```python
# 'DEFAULT_AUTHENTICATION_CLASSES': (
#     'rest_framework_simplejwt.authentication.JWTAuthentication',
# ),
```
По умолчанию используется стандартная DRF.

**Документация проекта** по доступным эндпоинтам и методам доступна после запуска по адресу:
```
http://127.0.0.1:8000/swagger
```

---

**1-й способ: Докер**
1. Выполнить в корневой директории
```shell
docker compose up
```
2. Сервис доступен по адресу
```
http://127.0.0.1:8000
```

**2-й способ: Локально (Команды для linux)**
1. Создать `venv` окружение

2. Установить зависимости:
```shell
pip install -r requirements.txt
```

3. Выполнить миграции:
```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

4. Запустить сервер:
```shell
python3 manage.py runserver
```

5. Сервис доступен по адресу:
```
http://127.0.0.1:8000
```
