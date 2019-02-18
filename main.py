#!/usr/bin/env python
# Telegram RPG Character Sheet bot

from pprint import pprint
import telepot
import time
import socket
import os
import re
import sys
import json
import random

import config
import db

log_file = 'service.log'


class Operation:
    def __init__(self, id, type, name):
        self.id = id
        self.type = type
        self.name = name
    def __eq__(self, other):
        return self.id == other.id

def die():
    os.kill(os.getpid(), signal.SIGINT)

def fatal(msg):
    print(msg)
    die()

def log(msg):
    f = open(log_file, 'a')
    f.write(msg + "\n")
    f.close()
    print(msg)

def log_msg(msg):
    chat_name = ''
    username = msg['from']['username']
    text = msg['text']
    if 'title' in msg['chat']:
        chat_name = '{} ({})'.format(msg['chat']['title'], username)
    else:
        chat_name = username
    log('{}: {}'.format(chat_name, text))
    
def send(bot, chat_id, msg):
    if msg == None or len(msg) == 0 or len(msg.split()) == 0:
        msg = '(no message)'
    bot.sendMessage(chat_id, msg)

def process_message(msg):
    """
    Process received messages.

    msg -- The received message
    """
    chat_id = msg['chat']['id']
    sender_id = msg['from']['id']
    username = msg['from']['username']
    text = msg['text']
    is_group = msg['chat']['type'] == 'group'
    groupname = msg['chat']['title'] if 'title' in msg['chat'] else None

    # avoid logging and processing every single message.
    if text[0] != '/':
        return

    log_msg(msg)
    dbc = db.open_connection()
    is_admin = False
    if sender_id in config.admins:
       is_admin = True

    args=text.split(maxsplit=1)
    command = args[0]
    if command == '/newgame':
        if not is_group:
            send(bot, chat_id, 'You must run this command in a group.')
            return
        if len(args) < 2:
            send(bot, chat_id, 'Please specify the game name.')
            return
        if db.number_of_games(dbc, sender_id) > 10:
            send(bot, chat_id, 'You exceeded the maximum number of games. Please close some first.')
            return
        db.new_game(dbc, sender_id, username, args[1], chat_id, groupname)
        send(bot, chat_id, 'New game created: {}.'.format(args[1]))
    if command == '/delgame':
        if not is_group:
            send(bot, chat_id, 'You must run this command in a group.')
            return
        # TODO
        if not is_admin:
            send(bot, chat_id, 'You need to be the administrator to close a game.')
            return
        gameid = db.get_game_from_group(dbc, chat_id)
        if gameid is None:
            send(bot, chat_id, 'No game found.')
            return
        db.del_game(dbc, gameid)
        send(bot, chat_id, 'GG, humans.')
    if command == '/showgame':
        if not is_group:
            send(bot, chat_id, 'You must run this command in a group.')
            return
        gameid = db.get_game_from_group(dbc, chat_id)
        gamename, groups, players = db.get_game_info(dbc, gameid)
        ret = '{}\nGroups: {}\nPlayers: {}'.format(gamename, ', '.join(groups), ', '.join(players))
        send(bot, chat_id, ret)

    if command == '/roll':
        ret = 0
        string = ''
        for i in range(0, 4):
            value = random.randint(-1, 1)
            ret += value;
            if value == -1:
                string += '➖'
            if value == 0:
                string += '〇'
            if value == 1:
                string += '➕'
        send(bot, chat_id, 'Rolled {} = {}.'.format(string, ret))

    if command == '/player':
        if not is_group:
            send(bot, chat_id, 'You must run this command in a group.')
            return
        if len(args) < 2:
            send(bot, chat_id, 'Please specify the player name.')
            return
        if db.number_of_games(dbc, sender_id) > 10:
            send(bot, chat_id, 'You exceeded the maximum number of games. Please close some first.')
            return
        gameid = db.get_game_from_group(dbc, chat_id)
        db.add_player(dbc, sender_id, args[1], gameid, db.ROLE_PLAYER)
        send(bot, chat_id, 'Welcome, {}.'.format(args[1]))

    if command == '/update' or command == '/add':
        if not is_group:
            send(bot, chat_id, 'You must run this command in a group.')
            return
        gameid = db.get_game_from_group(dbc, chat_id)
        if db.number_of_items(dbc, gameid, sender_id) > 50:
            send(bot, chat_id, 'You exceeded the maximum number of items. Please delete some first.')
            return
        args = args[1].split()
        if len(args) != 3:
            send(bot, chat_id, 'Use the format: [container] [key] [change].')
            return
        (container, key, change) = args
        if command == '/update':
            relative = False
        else:
            relative = True
        oldvalue, newvalue = db.update_item(dbc, gameid, sender_id, container, key, int(change), relative=relative)
        send(bot, chat_id, 'Updated {}/{} from {} to {} (changed {}).'.format(container, key, 
             oldvalue, newvalue, newvalue-oldvalue))
    if command == '/del':
        if not is_group:
            send(bot, chat_id, 'You must run this command in a group.')
            return
        gameid = db.get_game_from_group(dbc, chat_id)
        args = args[1].split()
        if len(args) != 2:
            send(bot, chat_id, 'Use the format: [container] [key].')
            return
        (container, key) = args
        oldvalue = db.delete_item(dbc, gameid, sender_id, container, key)
        if oldvalue == None:
            send(bot, chat_id, 'No item by that name.')
        else:
            send(bot, chat_id, 'Deleted {}/{} (was {}).'.format(container, key, oldvalue))

    if command == '/show':
        if not is_group:
            send(bot, chat_id, 'You must run this command in a group.')
            return
        gameid = db.get_game_from_group(dbc, chat_id)
        items = db.get_items(dbc, gameid, sender_id)
        ret = ''
        if items is None:
            send(bot, chat_id, 'No items found.')
            return
        for container in items:
            ret += container + ':\n'
            for key, value in items[container].items():
                ret += '  - {} ({})\n'.format(key,value)
        send(bot, chat_id, ret)

    db.close_connection(dbc)

db.init()
bot = telepot.Bot(config.bot_token)
print('Entering message loop.')
bot.message_loop(process_message)

while 1:
    time.sleep(10)
