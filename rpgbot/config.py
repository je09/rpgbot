import os
import importlib

admins = None
bot_token = None
db_file = None
log_file = None
language = None
phrase = None

try:
    # Import config from custom_config if present
    import custom_config
    admins = custom_config.admins
    bot_token = custom_config.bot_token
    db_file = custom_config.db_file
    log_file = custom_config.log_file
    language = custom_config.language
except:
    # Import config from env vars
    admins = os.environ.get('RPGBOT_ADMINS', '')
    if admins is None:
        raise Exception('No Admins Provided')

    admins = admins.split(',')

    bot_token = os.environ.get('RPGBOT_TOKEN')
    if bot_token is None:
        raise Exception('No Token Provided')

    db_file = os.environ.get('RPGBOT_DB_FILE', '/data/games.db' )

    log_file = os.environ.get('RPGBOT_LOG', '/data/service.log' )

    language = os.environ.get('RPGBOT_LANG', 'en')

try:
    phrase = importlib.import_module('langs.{}'.format(language))
except ModuleNotFoundError:
    raise Exception('Language file isn\'t found. Check the langs folder.')
