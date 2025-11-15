# Тестовое задание Uptrader

## Используемые технологии

Бэкенд: python3.10, django,

СУБД: PostgreSQL

Линтеры: isort, flake8

## Настройка проекта

Проект настраивается через переменные окружения, указанные в файле src/.env

Пример .env файла указан в .env.example:

| Ключ                            | Значение/Описание                            | По умолчанию (пример) |
|---------------------------------|----------------------------------------------|-----------------------|
| `SECRET_KEY`                    | Секретный ключ Django                        | `the-most-secret-key` |
| `DEBUG`                         | Режим дебага                                 | `True`                |
| `POSTGRES_DB`                   | Имя базы данных                              | `uptrader`            |
| `POSTGRES_USER`                 | Пользователь БД                              | `postgres`            |
| `POSTGRES_PASSWORD`             | Пароль пользователя БД                       | `postgres`            |
| `POSTGRES_HOST`                 | Адрес СУБД                                   | `db` / `localhost`    |
| `POSTGRES_PORT`                 | Порт СУБД                                    | `5432`                |


**Локальный разворот проекта**:

1) В директории проекта создать виртуальное окружение python3.10:
   `python3.10 -m venv venv`
2) Активировать виртуальное окружение:
   `. venv/bin/activate` для Linux или `.\venv\Scripts\activate` для Windows
3) Установить зависимости для проекта `pip install -r src/requirements.txt`
4) Развернуть базу данных `sudo docker-compose -f docker-compose.yml up db` или подключить локально
5) Заполнить содержимое файла src/.env по примеру в в src/.env.example
6) Перейти в папку src: `cd src`
7) Запустить django миграции: `python manage.py migrate`
8) Создать суперпользователя django: `python manage.py createsuperuser` (для использования в локальной разработке)
9) Запустить django server: `python manage.py runserver`

Проверка на линтеры, перейти в папку src:

1) `flake8`
2) `isort .`
