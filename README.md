# Base Django

**Описание:** базовый проект на Django. Использовался стандартный Django 5.2.8, Pillow для картинок
без создания кастомного юзер модели

Основной функционал: 
- авторизация
- регистрация
- страница профиля
- добавить фотографию
- смотреть фотографии
- удалить фотографию

## Список улучшений

- оформить красивую галерею на странице профиля
- использовать библиотеку Pillow
- создать общий templates в корне проекта
- создать отдельную ветку для generic views

## Установить зависимости

```bash
pip install -r requirements.txt
```

## Создать виртуальное окружение
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

```bash
python manage.py flush
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