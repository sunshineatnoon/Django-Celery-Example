# Django-Celery-Example
This is a simple example about integrating Celery in Django website, it uses celery to run a long task and shows a progress bar about the progress of the task.

![image](https://raw.githubusercontent.com/sunshineatnoon/Django-Celery-Example/master/images/2.png)
![image](https://raw.githubusercontent.com/sunshineatnoon/Django-Celery-Example/master/images/3.png)
![image](https://raw.githubusercontent.com/sunshineatnoon/Django-Celery-Example/master/images/1.png)


# Dependecies

Celery

Django

RabbitMQ

# How to run:

```
  git clone https://github.com/sunshineatnoon/Django-Celery-Example.git
  cd Django-Celery-Example
  /usr/local/sbin/rabbitmq-server
  celery -A celery_try worker -l info
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```

Then visit [http://127.0.0.1:8000/index/](http://127.0.0.1:8000/index/).
