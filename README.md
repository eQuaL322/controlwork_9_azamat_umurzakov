приложение "Галерея", которое позволяет своим пользователям загружать фотографии, просматривать их,
редактировать, удалять и добавлять в избранное.


superuser: login - root password - root
user: login - root2 password - root2

API для Photos:

'api/photos/' по этому адресу доступны все фото из галереи метод GET.
'api/login/' по этому адресу доступная авторизация.
'api/favorites/add/pk/' по этому адресу добавляется фото в избранное методом POST.
'api/favorites/remove/pk/ по этому адресу elftybt фото из избранного методом DELETE.

Локальный запуск проекта

После клонирования проекта выполните команды:

Создайте виртуальное окружение командой

python -m venv venv
Активируйте виртуальное окружение командой

source venv/bin/activate
venv\Scripts\activate
Установите зависимости командой

pip install -r requirements.txt
Перейдите в папку source командой

cd source
Примените миграции командой

python manage.py migrate
Запустите проект командой

Далее 
python3 manage.py loaddata > fixtures/dump.json

python manage.py runserver



