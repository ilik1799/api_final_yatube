# API для Yatube

Проект "API для Yatube" представляет собой API-интерфейс для социальной сети Yatube. Он позволяет разработчикам создавать и взаимодействовать с постами, комментариями, подписками и другими элементами функционала Yatube через стандартные HTTP-запросы.

## Установка

1. Склонируйте репозиторий `api_final_yatube` на вашем компьютере.

   git clone https://github.com/ilik1799/api_final_yatube.git


2. Перейдите в папку проекта
   
   cd api_final_yatube


3. Установите все необходимые пакеты из файла зависимостей
   
   pip install -r requirements.txt
  

4. Выполните миграции базы данных:
   
   python manage.py migrate
  

5. Запустите сервер разработки:
   
   python manage.py runserver