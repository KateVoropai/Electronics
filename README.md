# Electronics
Это веб-приложение на Django для управления сетью продаж электроники. Оно включает в себя API-интерфейс и панель администратора для управления различными уровнями иерархии сети, 
такими как заводы, дистрибьюторы, розничные сети и индивидуальные предприниматели.

## Requirements

- Python 3.8+
- Django 2.1+
- Django REST Framework (DRF) 3.10+
- Celery 4.4+
- PostgreSQL 10+
- Pipenv

## Environment Variables

Создайте файл `.env` в корне проекта с следующими переменными окружения:

DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

SECRET_KEY=your_django_secret_key
DEBUG=True  # Или False в production
ALLOWED_HOSTS=localhost, 127.0.0.1  

Установка
Склонируйте репозиторий:
git clone https://github.com/yourusername/electronics-sales-network.git
cd electronics_network

Установите зависимости, используя Pipenv:
pipenv install
