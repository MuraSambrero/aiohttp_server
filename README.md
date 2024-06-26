## Aiohttp- сервер

### Ендпоинты
- `/healthcheck`
- `/hash`

### Выполненные задачи
- [x] Задача 1. Создание базового API
- [x] Задача 2. Создание API для хеширования
- [x] Задача 3. Создание точки входа для запуска сервера
- [x] Задача 4. Создание Dockerfile
- [x] Задача 5. Написание тестов

### Запуск
1. Первым делом создайте файл `.env`.
2. Создайте в нем переменные `CELERY_RESULT_BACKEND` и `CELERY_BROKER_URL`.
3. Запустите контейниризированную среду.
Команда - `docker-compose up`.

Будут запущены три сервиса:
- redis(Поднимаем БД Redis для создания и обработки задача)
- web (Поднимаем http сервер)
- worker(С помощью Celery создаем worker для параллельного расчета hash)

### Redis и Celery
В данном приложении расчет hash происходит параллельно. Это было сделано в связи с тем, что hash функция расчитывается не так быстро. С помощью создания новых worker'ов мы создаем дополнительные процессы и тем самым ускоряем работу приложения(в масштабе).

