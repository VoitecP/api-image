# Django Rest Framework API Based, Upload Images
- Django 4.0 based, DRF API
- URL Router and Nested Router
- Two types of API
- Docker included
- Class based View's
- Clean Code
- Automatic Install Script and RUN
- Initial data auto import
- ( In development progress ) 


Any sugesstions and ideas to improve or expand this aplication will welcome.


# Demo screens
![image](https://github.com/VoitecP/api-image/blob/6e2d3c6127358708f06928b2522adcc33a1cb636/Demo%20images/demo1.jpg)
![image](https://github.com/VoitecP/api-image/blob/6e2d3c6127358708f06928b2522adcc33a1cb636/Demo%20images/demo2.jpg)
![image](https://github.com/VoitecP/api-image/blob/6e2d3c6127358708f06928b2522adcc33a1cb636/Demo%20images/demo3.jpg)

## How To Setup
```
git clone https://github.com/VoitecP/api-image.git
```
```
cd api-image/api_image/
```
```
Execute run-app.bat  
```

BAT Script will automatic Install Venv and Run server ! :)
But if you want to run manually, do as follow:

```
Create Virtual Enviroment in Python and activate
```
py -m venv env
```
```
source env/bin/activate
```
```
pip install -r requirements.txt
```
You need to create  Enviroment file .env 
```

Create .env file setting in base dir api_image  open .env file and paste SECRET_KEY='your_key', set DEBUG=1 save file. Env-Template file will help you .

```
Test database are already included ! Just clone and try :)
```

Load initial data to database

```
py manage.py cmd_fixtures
```
py manage.py runserver
```

Project in Local Host server: http://127.0.0.1:8000/   or in Docker  http://192.168.99.100:8000
