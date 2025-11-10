# Base Django

Основной функционал: 
- авторизация
- регистрация
- добавить фотографию
- страница профиля

## Установить зависимости

```bash
pip install -r requirements.txt
```

## Создать вирутальное окружение
```bash
python -m venv <name_venv>
```


## Django команды

#### Запустить проект

```bash
python manage.py runserver
```

#### Команды для БД
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

#### Команды крейторы

```bash
django-admin createproject <name_project>
```

```bash
python manage.py startapp <name_app>
```

```bash
python manage.py createsuperuser
```