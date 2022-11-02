## Настройка:

- Установка всех зависимостей из './requirements.txt'

- Подключение postgresql
  - Установка и создание postgresql базы данных
  - Создание таблицы с полями:
    - id (PK)
    - name (varchar, not null)
    - description (varchar, not null)
    - hash (integer, nullable)
  - Настройка переменных для подключения в файле './database/config.json'

## Запуск

Запуск файла './main.py'