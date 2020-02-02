FROM  python:3.7-buster

COPY requirements.txt /
COPY rpgbot /rpgbot
VOLUME /data
WORKDIR /rpgbot

CMD python /rpgbot/main.py
