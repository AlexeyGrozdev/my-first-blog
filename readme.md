# Roadmap практики:

## Важно знать
PEP8, импорты, нейминги, тайпинги

## Процесс работы
1. Установка: python 3.11, pip, pycharm community edition, venv; через requirements: django, rest framework, drf-nested-routers
2. Подготовка проекта, в режиме venv: выбор папки проекта <имя_проекта> -> "django-admin startproject <имя_проекта>"
3. Настраиваем корневые файлы:setting,urls
4. Первый запуск локального сервера: "python manage.py runserver". Конфигурация pycharm под быстрое выполнение команды (будем использовать её постоянно)
5. Подготовка приложения: "python manage.py startapp <имя_приложения>" (далее - blog); обновить settings
6. Создаём модели, например Post, и прописываем свойства и методы
7. Создаём скрипты для миграции (т.е. создаём таблицу моделей): mm.bat и m.bat : <CALL python manage.py makemigrations blog> и <CALL python manage.py migrate blog>. Каждый следующий раз мигрируем свои изменения запуская батники
8. Добавим суперпользователя для нашего проекта: меняем blog/admin.py; "python manage.py createsuperuser"
9. Добавим новые посты через нативную админ панель django на localhost:8000/admin. (опционально): работаем над фронтом
10. Создаём папку api с файлами urls, views, serializers и прописываем их: 
    * views: Классы обработчики запросов для работы с моделями, получение querry lists и запрос сериалайзинга
    * urls: роутеры и шаблоны для работы с url приложения
    * serializers: прописываем сериалайзинг моделей
11. Создаём nested модели commentPost, LikePost, LikeComment. Создаём для каждого свои url, serializer и view; мигрируем.
12. Учимся объединять миграции: Откатываемся (migrate) до zero, удаляем все миграции, создаём новую 
13. Создаём точки доступа во view: actions на get, post, put, delete