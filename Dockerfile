FROM  python:3.7-slim-buster

COPY requirements.txt /

RUN pip install -r requirements.txt

RUN mkdir /rpgbot

COPY main.py /rpgbot
COPY db.py /rpgbot
COPY config.py /rpgbot
COPY langs/ /rpgbot/langs/
COPY commands.py /rpgbot
COPY diceroller.py /rpgbot
COPY keyboard.py /rpgbot

VOLUME /data

WORKDIR /rpgbot

CMD python /rpgbot/main.py
