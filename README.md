# Social network back-end with graphql
This project is a demo of a Django service with Graphql to create simple social network back-end 📷.

### Run this project locally:
- Install dependencies using `pipenv install`
- Start the virtual environment by `pipenv shell`.
- Enter to the main directory `cd web_service`.
- Run the current migrations `python manage.py migrate`.
- Add a superuser `python manage.py createsuperuser`.
- Run the local django server using `python manage.py runserver`.
- The services is pointing to the url `http://localhost:8000/`.

### Run this project using docker-compose:
- Enter to the docker directory.
- Run `docker-compose build` to create the docker image.
- Run the current migrations `docker-compose run web_service python manage.py migrate`.
- Add a superuser `python manage.py createsuperuser`.
- Run the project using `docker-compose up -d`.
- The services is pointing to the url `http://localhost:8000/`.
