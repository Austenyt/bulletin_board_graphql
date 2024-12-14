# Bulletin Board API

Данный проект представляет собой API для доски объявлений, реализованный с использованием Django и GraphQL. Он позволяет пользователям создавать, читать и фильтровать объявления по заголовку и хэштегам.

## Технологии

- **Django**: веб-фреймворк для создания веб-приложений на Python.
- **Graphene-Django**: библиотека для интеграции GraphQL с Django.
- **Python**: язык программирования, используемый для разработки.

## Подготовка

**Убедитесь, что у вас установлен Python**. Вы можете проверить это, выполнив команду:

- Для Windows и Linux:

   ```bash
   python --version
   
- Для Mac:

   ```bash
   python3 --version
  
## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/Austenyt/bulletin_board_graphql.git
   cd ваш_репозиторий
   
2. Создайте виртуальное окружение. Перейдите в корневую директорию вашего проекта и выполните команду:

    ```bash
    python -m venv venv
   
3. Установите зависимости:

    ```bash
    pip install -r requirements.txt

4. Переименуйте файл .env.sample в .env и заполните соответствующие поля.
5. Зайдите в диалог работы с базами данных:

    ```bash
    psql -U postgres

6. Создайте базу данных:

    ```bash
    CREATE DATABASE имя БД;

7. Выполните миграции базы данных:

    ```bash
    python manage.py migrate

8. Заполните базу данных из JSON-файла, который содержит несколько объявлений для примера:

    ```bash
    python manage.py loaddata bulletins.json
   
9. Запустите сервер разработки:

    ```bash
    python manage.py runserver

10. Для добавления новых объявлений можно использовать, например, admin-панель Django. Для этого создайте суперпользователя командой

    ```bash
    python manage.py createsuperuser
    
Админ-панель доступна по адресу http://127.0.0.1:8000/admin. Через нее можно добавить объявления, хэштэги вводятся через запятую.
Для работы с запросами можно использовать собственный браузер Graphiql по адресу http://127.0.0.1:8000/graphql/ или клиент, например Postman.

## Использование
### API предоставляет следующие запросы:

- #### Получить все объявления:

```
query {
    allBulletins {
        id
        title
        description
        price
        hashtags
    }
}
```

- #### Получить объявления по заголовку:

```
query {
  bulletinsByTitle(title: "ваш заголовок") {
    id
    title
    description
    price
    hashtags
  }
}
```

- #### Получить объявления по хэштегу:

```
query {
  bulletinsByHashtag(hashtag: "#ваш_хэштег") {
    id
    title
    description
    price
    hashtags
  }
}
```

## Структура проекта
- bulletins/: приложение Django, содержащее модели и GraphQL-схему.
- models.py: содержит модель Bulletin, представляющую объявление.
- schema.py: определяет GraphQL-схему и запросы.

## Вклад
Если вы хотите внести свой вклад в проект, пожалуйста, используйте ветку develop для вашей функции или исправления, а затем создайте пулл-запрос.