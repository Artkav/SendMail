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
    https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa1ZxeUFPVWp3RVRoeEJRTEJDbDBxVE9yQkN4QXxBQ3Jtc0tuN2NseFRjNTlJbnVVWGZzeTNIekI5ajBPUXliVkRsN01xVkZLR2RIQXNBamMyN1lTQ1FKZFpuMThfeVYyUnJhQ0h1VzdOajdfQWdzS09SR2hHano5RFhNWlRhdURPOG1Vbm1sa0t6TGhRWlpBc0pWbw&q=https%3A%2F%2Fmyaccount.google.com%2Fu%2F0%2Flesssecureapps  

#### 7) Запустить сервер
    python manage.py runserver
