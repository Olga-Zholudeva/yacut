# Сервис Yacut

## Суть проекта:

Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис. Вы можете получить короткую ссылку через веб-интерфейс или посредством запроса к API

## Технологии проекта:

- Python 3.7.9
- Flask 2.0.2

## Запуск проекта на локальном компьютере:

- Клонируем репозиторий: git clone [Сервис Yacut](https://github.com/Olga-Zholudeva/yacut)
- Cоздаем и активировируем виртуальное окружение: python3 -m venv env source env/bin/activate
- Устанавливаем зависимости из файла requirements.txt: pip install -r requirements.txt
- Выполняем миграции: **flask db upgrade**
- Запускаем проект: **flask run**

## Получение ссылки через веб-интерфейс:

- После запуска проект доступен по ссылке: **http://127.0.0.1:5000**
- Заполняем поле **Длинная ссылка**
- Можно заполнить поле **Ваш вариант короткой ссылки** либо оставить его пустым (ссылка будет сгенерирована автоматически)

## Получение ссылки через запросы к API:  

- POST запрос на создание ссылки:  
    **эндпоинт:** /api/id/  
    **пример запроса:**  
        {  
        "url": "string",  
        "custom_id": "string"  
        }  
    **пример ответа:**  
        {  
        "url": "string",  
        "short_link": "string"  
        }  
- GET запрос на получение длинной ссылки по короткой:  
    **эндпоинт:** /api/id/{short_id}/  
    **пример ответа:**  
        {  
        "url": "string"  
        }
  
Более детальная информация в спецификации openapi.yml
Для удобства использования можно воспользоваться [онлайн-редактором Swagger Editor](https://editor.swagger.io/), в котором можно визуализировать спецификацию.

## Проект выполнен:

**Ольга Жолудева**
