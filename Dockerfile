FROM python:3.8.3-alpine
WORKDIR /app
RUN pip install --upgrade pip 
COPY /myproject .
RUN pip install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]