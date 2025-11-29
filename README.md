## Структура проекта
### Backend (Django)
-    `/server/`: Корневая папка бэкенда

-    `/server/app/`: Основное Django приложение

-    `/server/app/migrations/`: Миграции базы данных

-    `/server/app/models.py`: Модели данных (Person, Course, Assignment, Submission)

-    `/server/app/views.py`: API endpoints и бизнес-логика

-    `/server/app/serializers.py`: Сериализаторы для REST API

-    `/server/app/urls.py`: URL маршруты приложения

-    `/server/app/admin.py`: Настройки админ-панели Django

-    `/server/psb_campus/`: Настройки проекта Django

-    `/server/psb_campus/settings.py`: Конфигурация Django

-    `/server/psb_campus/urls.py`: Главные URL маршруты

-   `-/server/manage.py`: Утилита управления Django

-    `/server/db.sqlite3`: База данных SQLite

-    `/server/requirements.txt`: Зависимости Python


## Версии 
- Django==5.2.8
- djangorestframework==3.15.1
- django-cors-headers==4.4.0
- Pillow==10.3.0
