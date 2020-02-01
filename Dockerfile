FROM  python:3.7-buster

COPY requirements.txt /
<<<<<<< HEAD
RUN pip install -r requirements.txt
=======
RUN pip install -r requirements.txt; \
    apt-get update; \
    apt-get install tor privoxy -y; \
    echo "forward-socks5t / 127.0.0.1:9050 ." >> /etc/privoxy/config; \
    service privoxy restart;

>>>>>>> 34100f3734b3626471289c885f992b5bd72231f6
COPY rpgbot /rpgbot
VOLUME /data
WORKDIR /rpgbot

CMD python /rpgbot/main.py
