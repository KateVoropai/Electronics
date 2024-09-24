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

DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432

SECRET_KEY='django-insecure-(yyf71$a3j&795)9b($*5g=26e^o2u#ea)_rvs_&7$fnvk)bui'
DEBUG=True  # Или False в production
ALLOWED_HOSTS=localhost, 127.0.0.1  

Установка
Склонируйте репозиторий:
git clone https://github.com/yourusername/electronics-sales-network.git
cd electronics_network

Установите зависимости, используя Pipenv:
pipenv install
