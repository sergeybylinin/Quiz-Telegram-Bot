# Quiz-Telegram-Bot

Quiz-Telegram-Bot — это Telegram-бот для проведения викторин. Бот задает пользователю вопросы с вариантами ответов, проверяет правильность ответов и ведет учет результатов. Проект написан на Python с использованием библиотеки `aiogram` для работы с Telegram API и `aiosqlite` для работы с базой данных.

---

## Функциональность

- **Старт викторины:** Пользователь может начать викторину, отправив команду `/quiz` или нажав кнопку "Начать игру".
- **Вопросы и ответы:** Бот задает вопросы с вариантами ответов. Пользователь выбирает один из предложенных вариантов.
- **Проверка ответов:** Бот проверяет правильность ответа и сообщает результат.
- **Результаты:** Пользователь может узнать свои результаты, отправив команду `/result` или нажав кнопку "Результаты".
- **Хранение данных:** Результаты и прогресс пользователя сохраняются в базе данных SQLite.

---

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/ваш-репозиторий/Quiz-Telegram-Bot.git
cd Quiz-Telegram-Bot
```

### 2. Установка зависимостей
Убедитесь, что у вас установлен Python 3.8 или выше. Затем установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

### 3. Настройка бота
1. Создайте файл input в корневой директории проекта и добавьте в него токен вашего бота:

```
BOT_TOKEN=ваш_токен_бота
```

2. Настройте вопросы викторины в файле data.py. Каждый вопрос должен содержать текст вопроса, варианты ответов и индекс правильного ответа.

### 4. Запуск бота
Запустите бота с помощью команды:

```bash
python main.py
```

---

## Структура проекта
* `data.py:` Содержит данные для викторины (вопросы, варианты ответов и правильные ответы).
* `settings.py:` Настройки бота, включая токен.
* `db.py:` Логика работы с базой данных SQLite.
* `main.py:` Основной файл, содержащий логику бота.
* `.gitignore:` Игнорируемые файлы, такие как база данных и токен бота.

---

## Используемые технологии
1. **Python:** Основной язык программирования.
2. **Aiogram:** Библиотека для работы с Telegram Bot API.
3. **SQLite:** База данных для хранения прогресса пользователей.
4. **Asyncio:** Для асинхронного выполнения задач.

---

## Пример работы
1. Пользователь запускает бота командой `/start`.
2. Бот предлагает начать викторину или посмотреть результаты.
3. Пользователь выбирает "Начать игру".
4. Бот задает вопросы, пользователь выбирает ответы.
5. После завершения викторины бот показывает результаты.

## Благодарности
* Спасибо aiogram за отличную библиотеку для работы с Telegram API.
* Спасибо SQLite за простую и надежную базу данных.
