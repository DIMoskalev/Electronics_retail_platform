# Онлайн платформа-торговая сеть электроники
## Описание проекта
Данный проект представляет собой онлайн платформу для торговли электроникой, реализованную с использованием Django и Django REST Framework. Платформа позволяет управлять иерархической структурой торговли электроникой, которая включает заводы, розничные сети и индивидуальных предпринимателей.

## Стек технологий
- **Python 3.8+**
- **Django 3+**
- **Django REST Framework 3.10+**
- **PostgreSQL 10+**

## Основные требования и функциональные возможности
### 1. Иерархическая модель:

Модель сети по продаже электроники, представляет собой следующую иерархическую структуру из трех уровней (Каждое звено может ссылаться только на одного поставщика оборудования):
- Завод (уровень 0)
- Розничная сеть (уровень 1)
- Индивидуальный предприниматель (уровень 2)


### 2. Поля модели:

  - **Название**
  - **Контакты:**
    - email,
    - страна,
    - город,
    - улица,
    - номер дома.
    
  - **Продукты:**
    - название,
    - модель,
    - дата выхода продукта на рынок.
  - **Поставщик (предыдущий по иерархии объект сети).**
  - **Задолженность перед поставщиком в денежном выражении с точностью до копеек.**
  - **Время создания (автоматически заполняется при создании).**
### 3. Админ-панель:

- **Вывод созданных объектов в админ-панели.**
- **Добавлена ссылка на «Поставщика» на странице объекта сети.**
- **Фильтрация объектов по названию города.**
- **Admin action, позволяющий очищать задолженность перед поставщиком у выбранных объектов.**

### 4. API-интерфейс (DRF):

- **Создать набор представлений для CRUD операций над моделью поставщика.**
- **Запретить обновление поля «Задолженность перед поставщиком» через API.**
- **Добавить возможность фильтрации объектов по стране.**

### 5. Безопасность и права доступа:

- Настроены права доступа к API так, чтобы только активные сотрудники имели доступ к API.

## Установка и настройка

- **1.Клонируйте репозиторий:**

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

- **2.Создайте и активируйте виртуальное окружение:**

```bash
python -m venv venv
source venv/bin/activate   # Для Unix/Mac
```

- **3. Установите зависимости:**

```bash
pip install -r requirements.txt
```

- **4. Настройте базу данных:**
  - Создайте файл .env на основе .env.example и добавьте необходимые переменные окружения.

- **5. Примените миграции:**

```bash
python manage.py migrate
```

- **6. Создате суперпользователя для доступа к админ-панели:**
```bash
python manage.py csu
```

- **7. Запустите сервер:**
```bash
python manage.py runserver
```

## Использование
- Для доступа к админ-панели зайдите по адресу: http://127.0.0.1:8000/admin.
- Используйте API для взаимодействия с данными о поставщиках и объектах сети.
- Документация API доступна по адресам:
    - Swagger - http://localhost:8000/swagger/
    - Redoc - http://localhost:8000/redoc/