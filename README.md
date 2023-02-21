# STRIPE_DJANGO
В данном проекте реализован сервер на базе Django, который общается со Stripe и создает платёжные формы для товаров.


## Технологии
- [Stripe](https://stripe.com/)
- [Django](https://www.djangoproject.com/)

## Установка 
1. При помощи утилиты Git, загрузите данный репозиторий в вашу папку с проектами:
```sh
$ git clone https://github.com/Holm1997/STRIPE_DJANGO.git
```

2. Окройте папку с проектом в VS Code


3. В папке STRIPE_DJANGO в терминали установите виртуальное окружение: 
```sh
python -m venv venv
```

4. Активируйте виртуальное окружение:
```sh
venv/scripts/activate
```

4. Установите библиотеки Django и Stripe:
```sh
pip install -r requirements.txt
```

5. Запустите сервер для разработки Django:
```sh
cd main

python manage.py runserver
```