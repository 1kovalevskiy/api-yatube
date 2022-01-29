# Сервис YatubeAPI
![yatube](https://github.com/1kovalevskiy/api-yatube/actions/workflows/main.yml/badge.svg)
![coverage](https://github.com/1kovalevskiy/api-yatube/blob/master/coverage.svg)

## Учебный сервис "Yatube" Личные блоги
Это проект, на котором можно создать свою страницу.
Если на нее зайти, то можно посмотреть все записи автора.
Пользователи могут заходить на чужие страницы, подписываться на авторов и комментировать их записи.
Автор может выбрать имя и уникальный адрес для своей страницы.
Есть возможность модерировать записи и блокировать пользователей, если начнут присылать спам.
Записи можно отправить в сообщество и посмотреть там записи разных авторов.

## Deploy
В корневой папке 
- Создать файл `.env` по примеру файла `.env.sample`
- Запустить `docker-compose up -d`

## Тестовый сервер
[Тестовый сервер (не работает)](http://api-yatube.kovalevskiy.xyz)http://api-yatube.kovalevskiy.xyz

## Технологии
- API на "Django + DRF"
- Тестирование на "Pytest"
- БД PostgreSQL
- Proxy Nginx
- Контейнеризация с помощью Docker
