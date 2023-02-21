# STRIPE_DJANGO
В данном проекте реализован сервер на базе Django, который общается со Stripe и создает платёжные формы для товаров.

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)

## Технологии
- [Stripe](https://stripe.com/)
- [Django](https://www.djangoproject.com/)

## Использование
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


## Разработка

### Требования
Для установки и запуска проекта, необходим [NodeJS](https://nodejs.org/) v8+.

### Установка зависимостей
Для установки зависимостей, выполните команду:
```sh
$ npm i
```

### Запуск Development сервера
Чтобы запустить сервер для разработки, выполните команду:
```sh
npm start
```

### Создание билда
Чтобы выполнить production сборку, выполните команду: 
```sh
npm run build
```

## Тестирование
Какие инструменты тестирования использованы в проекте и как их запускать. Например:

Наш проект покрыт юнит-тестами Jest. Для их запуска выполните команду:
```sh
npm run test
```

## Deploy и CI/CD
Расскажите, как развернуть приложение. Как запустить пайплайны и т.д.

## Contributing
Как помочь в разработке проекта? Как отправить предложение или баг-репорт. Как отправить доработку (оформить pull request, какие стайлгайды используются). Можно вынести в отдельный файл — [Contributing.md](./CONTRIBUTING.md).

## FAQ 
Если потребители вашего кода часто задают одни и те же вопросы, добавьте ответы на них в этом разделе.

### Зачем вы разработали этот проект?
Чтобы был.

## To do
- [x] Добавить крутое README
- [ ] Всё переписать
- [ ] ...

## Команда проекта
Оставьте пользователям контакты и инструкции, как связаться с командой разработки.

- [Богдан Звягинцев](tg://resolve?domain=bzvyagintsev) — Front-End Engineer

## Источники
Если вы чем-то вдохновлялись, расскажите об этом: где брали идеи, какие туториалы смотрели, ссылки на исходники кода. 
