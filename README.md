# Nexo: Your personal organizer

## An small but functional project dedicated to organize your life, written in Python


"Nexo" is an small web personal organizer with two principal functionalities: a contact list and a task manager. This project was built with Django and Semantic UI. The main purpose of this project is showing my developer abilities.

![Home preview](./preview_image/prev1.png)

## Installation instructions

1. Clone this project
2. Install the requirements
```
pip install -r requirements.txt
```
3. Go to folder `nexo_project`, remove `.example` to `.env.example` and change their values with yours.
4. Apply these commands
```
python manage.py migrate
python manage.py loaddata countries
```
5. Run the server
```
python manage.py runserver
```

## Contributors
Use this project as you wish. \
If you find a bug, improve this project. \
If you have a question, contact me