[Текст задания](https://github.com/polecie/test/blob/main/src/task.md)

Для удобства приложена db.sqlite3 база данных с предзаполненными данными

## Настройка окружения
При необходимости измените переменные окружения в .docker/etc/.env

## Запуск
Склонируйте репозиторий и в папке с проектом выполните команду `docker-compose -f .docker/docker-compose.yaml up -d --build`, после этого проект доступен на http://0.0.0.0:8000

Для создания суперпользователя можно использовать команду `docker compose -f .docker/docker-compose.yaml exec -it api python manage.py createsuperuser` или использовать готового суперпользователя с кредами `admin:admin`

## Оптимизация
- Используется `select_related` для оптимизации запросов `FK`
- Обновление счетчика просмотров с помощью `F`-выражений
