# SendMail
## Тренировочный проект для отправки текста через email
    Лучше использовать тестовый, а не основной электронный адрес

### Установка

#### 1) Создать виртуальное окружение

    python -m venv venv

#### 2) Активировать виртуальное окружение
   
#### 3) Устанавливить зависимости:
    pip install -r req.txt

#### 4) Выполнять миграции и создавать admin нет необходимости

#### 5) В папке sendemailproject/sendemailproject/ необходимо создать файл email_config.py в котором прописать:    
    EMAIL_HOST = 'smtp.gmail.com'     если электронна почта на google
    EMAIL_PORT = 587            если электронна почта на googl
    EMAIL_HOST_USER = 'email@gmai.com'      адрес электронной почты с которого будет производится отправка  
    EMAIL_HOST_PASSWORD = 'password123'     пароль от электронной почты
    
    Либо напрямую прописать данные параметры в файле settings.py после #SMTP Configuration
    
#### 6) Разрешить доступ ненадежным приложениям к электронной почте:
    https://myaccount.google.com/u/0/lesssecureapps?pli=1&rapt=AEjHL4PS54xt0hxedRIbrGZ0qeV0GmJkWOUb_5Aa7KV4bHJ4iNjA5NqzzCCfoOC3Nt-M4OxJeINmy9dOa9Ydvu84Nbf1Mby5gQ  

#### 7) Запустить сервер
    python manage.py runserver
