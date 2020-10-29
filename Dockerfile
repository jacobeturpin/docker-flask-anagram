FROM python:3.6.5-alpine

WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

CMD [ "python", "src/app.py"]