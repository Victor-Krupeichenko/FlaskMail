# FlaskMail
![Python](https://img.shields.io/badge/-Python-f1f518?style=flat-square&logo=python)
![Fkask](https://img.shields.io/badge/-Flask-74cf3c?style=flat-square&logo=flask) 
![Bootstrap](https://img.shields.io/badge/-Bootstrap-ce62f5?style=flat-square&logo=bootstrap)
![Celery](https://img.shields.io/badge/-Celery-37814A?style=flat-square&logo=Celery)  
![Docker](https://img.shields.io/badge/-Docker-1de4f2?style=flat-square&logo=docker)  
![Redis](https://img.shields.io/badge/-Redis-f78b97?style=flat-square&logo=redis)
![Postgresql](https://img.shields.io/badge/-Postgresql-1de4f2?style=flat-square&logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-ba7378?style=flat-square&logo=sqlalchemy)
![Alembic](https://img.shields.io/badge/-Alembic-80cced?style=flat-square&logo=Alembic)

Приложение для отправки email по списку получателей

- список получателей можно загрузить в форматах csv или json
- может формировать отчет в формате pdf(отчет можно скачать) о количестве отправленных email и получателей
- email можно отправлять как без вложения, так и прикрепить pdf файл
  (само по себе приложение разработалось для рассылки резюме)
- приложение использует технологию celery(с очередями: отправка email и формирование отчета)

Приложение состоит из трёх частей:
- mailing-отправка email
- recipient_list_file - получения списка получателей
- report - формирование pdf-отчета

## Установка

- необходимо создать в корне проекта файл .env в котором указать:
POSTGRES_DB=ваше_название_для базы данных
POSTGRES_HOST=weather_database
POSTGRES_USER=ваше_имя_пользователя
POSTGRES_PASSWORD=ваш_пароль
POSTGRES_PORT=(можете указать другой порт-тогда и в docker-compose.yml необходимо изменить на другой)
REDIS_HOST=redis_mail - если запускает через docker
REDIS_HOST=0.0.0.0 - если запускаете локально
REDIS_PORT=6112 - или укажите свой(тогда необходимо изменить и в docker-compose.yml)
REDIS_DB=0
SECRET_KEY_CSRF=секретный_ключ_для_csrf_токена
SMTP_USER=укажите_свой_email_адрес
SMTP_PASSWORD=укажите_свой_пароль_от_email_адреса
SMTP_HOST=хост_на_котором_расположен_ваш_email_адрес(например: smtp.gmail.com или smtp.yandex.ru)
SMTP_PORT=порт_который_позволяет_подключится_к_smtp(например: 465 или 587)

## Установка на локальный компьютер

- git clone https://github.com/Victor-Krupeichenko/FlaskMail.git
- pip install -r requirements.txt
- запуск через терминал:
- под linux export FLASK_APP=app.py
- flask run
- перейти по ссылке: http://127.0.0.1:5000

## Установка в docker

- git clone https://github.com/Victor-Krupeichenko/FlaskMail.git
- запуск через терминал(обязательно должны находится в папке проекта): docker compose up или docker-compose up
- перейти по ссылке: http://0.0.0.0:5000

## Структура проекта

В папке database находятся:
- подключение к базе данных, модель таблицы в базе данных

В папке docker_start(для запуска приложения в docker) находятся:
- bash-скрипт flower - для запуска мониторинга задач celery
- bash-скрипт start - для запуска alembic миграций для создания таблицы в базе данных, запуск celery и запуск самого приложения

В папке mailing находятся:
- форма получение данных от пользователя для формирования email
- представления для мониторинга получателей(сколько отправлено писем)
- представление для отправки email

В папке migrations находятся:
- alembic файл миграции для создания таблицы в базе данных
- настройки имен переменного окружения для подключения к базе данных

В папке recipient_list_file находятся:
- форма для загрузки списка получателей
- обработчики для csv и json файлов
- представление для получения из формы списка получателей
- вспомогательные функции

В папке report находятся:
- форма для запроса получателя по его имени
- представление для получения информации(в рамках сколько отправлено email, сам email-адрес), генерировать pdf-отчет и скачать его
- вспомогательные функции

В папке static находятся:
- статический файл для навигационной панели

В папке tasks находятся:
- настройки celery
- рассылка email, формирование отчета
- вспомогательная функция

В папке templates находятся:
- html-шаблоны
- в папке _inc находятся подключаемые html-шаблоны

alembic.ini содержит маршрут для подключения alembic к базе данных
docker-compose.yml содержит описание запуска проекта в docker
Dockerfile содержит инструкции для создания docker-образа
app.py запускает приложение
requirements.txt в нем находятся все необходимые для работы приложения библиотеки и зависимости
setting_env.py - настройки имен переменно окружения


## Контакты:

Виктор

# Email:

- krupeichenkovictor@gmail.com
- victor_krupeichenko@hotmail.com

# Viber:

- +375447031953 
