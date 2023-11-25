# Скрапер входу та профілю GitHub

Цей сценарій Python демонструє, як виконати вхід до GitHub за допомогою requestsбібліотеки з підробленим агентом користувача, створеним fake_useragent. Потім він витягує файли cookie із сеансу та використовує їх, щоб зробити другий запит для отримання інформації профілю користувача.

# передумови
Переконайтеся, що у вас встановлені необхідні бібліотеки. Ви можете встановити їх за допомогою наступного:
```bash
pip install requests fake_useragent beautifulsoup4
```

# Використання
1.Клонуйте репозиторій:
``` bash
git clone git@github.com:kozhydlo/GitHub-login-and-profile-scraper.git
```
2.Перейдіть до каталогу проекту
3.Запустіть сценарій

# Пояснення коду

## Імпорт бібліотек:

requests: Використовується для створення HTTP-запитів.
fake_useragent: генерує випадковий User-Agent для імітації різних браузерів.
BeautifulSoup: бібліотека для отримання даних із файлів HTML і XML.
## Налаштування сеансу:

Сеанс ( sessions) створюється для збереження певних параметрів у запитах, наприклад файлів cookie.

## Вхід в систему:

Сценарій виконує вхід до GitHub за допомогою наданого імені користувача та пароля.
Fake User-Agent встановлюється в заголовках, щоб імітувати справжній браузер.
Перевіряється статус відповіді, і якщо вхід пройшов успішно (код статусу 302), відбувається перенаправлення на сторінку профілю користувача.

## Отримання інформації профілю:

Файли cookie, отримані під час сеансу входу, витягуються та використовуються для налаштування нового сеансу ( session2).
Потім другий сеанс використовується для надсилання запиту на сторінку профілю користувача, а вміст HTML друкується.

# Примітка

Обов’язково замініть облікові дані заповнювачів `( loginі password) `вашим фактичним іменем користувача та паролем GitHub.

Цей сценарій призначено лише для освітніх цілей, і використання автоматизованих сценаріїв для взаємодії з веб-сайтами має відповідати умовам обслуговування сайту. Автоматизація взаємодії з веб-сайтом без дозволу може порушити його умови та призвести до блокування вашого облікового запису. Використовуйте цей скрипт відповідально та на власний ризик.
