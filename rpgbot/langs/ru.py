# commands.py
warning_game_already_exists = """Игра уже начата.
Самое время позвать игроков, попросите их сделать это с помощью `/player <character name>`, посмотреть своего персонажа `/show`, изменить что-либо `/update`, бросить дайсы `/roll`.
Полный список команд можно найти здесь: https://github.com/simonebaracchi/rpgbot."""
warning_run_in_group = 'Данная комнада выполняется только в группе.'
warning_one_game = 'Приносим свои извенения, но на данный момент, за раз доступна только одна игра.'
warning_no_game_found = 'Ни одна игра не найдена.'
warning_gm_role = 'Вы должны быть ГМ-ом, чтобы завершить игру.'
warning_maximum_item_number = 'Вы достигли максимально возможного количества предметов. Пожалуйста, удалите что-нибудь лишнее.'
warning_item_not_found = 'Предмет {}/{} не найден.'
warning_not_in_game = 'Вы не находитесь в игре.'
warning_no_items_found = 'Ни один предмет не найден.'
warning_less_dices = 'Не вышло. Пожалуйста, попробуйте с меньшим количеством дайсов.'
warning_invalid_dices = 'Неверный формат дайсов.'
warning_couldnt_send_dice_result = '{}, Я не смог отпраивть вам результаты броска. Пожалуйста, отправьте мне сообщение, чтобы разрешить отправлять вам сообщения.'

question_new_container_name = 'Как вы хотите назвать контейнер?'
question_new_game_name = 'Как вы хотите назвать игру?'
question_template = 'Пожалуйста, выберите шаблон для игры. Шаблон влияет на стиль листов характеристик и тип дайсов'
question_player_name = 'Как твое имя, авантюрист?'
question_container = 'В какой контейнер?'
question_add_item_key = 'Какой предмет вы хотите добавить?'
question_set_item_key = 'На что вы хотите это изменить?'
question_which_item_key = 'Какой предмет?'
question_which_player = 'Какого игрока?'
question_what_to_add = 'Что вы хотите добавить?'

message_welcome_bot = """Привет, человек.
Я character sheet bot для Fate RPG.
Для того, чтобы использовать меня, добавьте меня в группу, пригласите других игроков и напишите мне, когда будете готовы начать игру.
Для того чтобы получить доступ к моим функциям, можете использовать наэкранную клавиатуру или текстовые команды (`/roll` для того, чтобы бросить дайсы).
Для более получения более подробной информации, можете посетить мой официальный сайт.

Удачных игр!"""
message_game_created = 'Новая игра была создана: {}.'
message_del_game = 'GG, человеки.'
message_known_as = 'Вы будете известны, как {}.'
message_groups_players = '{} ({})\nГруппы: {}\nИгроки: {}'
message_room_aspects = '\nАспекты комнаты:\n{}'
message_welcome = 'Добро пожаловать, {}.'
message_updated_form = 'Обновил {}/{} с {} на {} (changed {}).'
message_updated = 'Обновил {}/{} на "{}".'
message_added = 'Добавил "{}" в контейнер {}.'
message_deleted_item = 'Удалил {}/{} (было {}).'
message_character_sheet = 'Характеристика {}:\n'
message_dice_rolled = 'Выпало {} = {}.'
message_gm_dice_rolled = '{} тайно пробросил {}...'
message_dice_you_rolled = 'У вас пыпало {} = {}.'
message_rolled = '{} ({}) выбросил {} = {}.'
message_suggest_new_game = """Приветсвую, Путники.
Я character-sheet-bot для Fate RPG.
Чем могу быть полезен?"""

keyboard_site = 'Перейти на оф. сайт ->'
keyboard_rooms_items = 'Предметы комнаты'
keyboard_saved_rolls = 'Сохраненные броски'
keyboard_new_container = 'Новый контейнер ...'
keyboard_join_game = 'Присоединиться к игре'
keyboard_roll_dices = 'Бросить дайс (/roll <dice>)'
keyboard_how_can_i_help = 'Чем я могу вам помочь?'
keyboard_new_game = 'Начать новую игру'
keyboard_game_status = 'Показать статус игры'
keyboard_player_status = 'Показать статус игрока'
keyboard_other_player_status = 'Показать статус других игроков'
keyboard_add_item = 'Добавить предмет'
keyboard_update_item = 'Обновить предмет'
keyboard_add_list_item = 'Добавить предмет списка'
keyboard_delete_item = 'Удалить предмет'
keyboard_roll_dices_gm = 'Тайно бросить дайс (/gmroll)'
keyboard_cancel = 'Отменить'
keyboard_more = 'Ещё ...'
keyboard_change_player_name = 'Изменить имя игрока'
keyboard_delete_game = 'Удалить игру'
keyboard_back = '<- Назад'


# keyboard.py
warning_too_late = 'Лимит времени истек.'
no_message = '(Нет новых сообщений)'


# db,py

#dnd
db_general = 'общее'
db_general_description = 'описание'
db_general_description_value = 'Опишите вашего персонажей парой слов.'
db_general_fatepoints = 'жетоны судьбы'
db_general_refresh = 'ед. обновления'
db_general_stress = 'стресс'
db_general_dnd_class = 'класс'
db_general_dnd_class_value = 'Ваш класс.'
db_general_race = 'расса'
db_general_race_value = 'Ваша расса.'
db_general_alignment = 'мировозрение'
db_general_alignment_value = 'Ваше мировозрение.'
db_general_level = 'уровень'
db_general_attributes = 'атрибуты'
db_general_attributes_strength = 'сила'
db_general_attributes_dexterity = 'ловкость'
db_general_attributes_constitution = 'телосложение'
db_general_attributes_intelligence = 'интеллект'
db_general_attributes_wisdom = 'мудрость'
db_general_attributes_charisma = 'харизма'

db_inactive = 'Неактивен'
db_stunts = 'трюки'
db_stunts_value = 'Здесь можно описать первый "трюк".'

db_aspects = 'аспекты'
db_aspects_highconcept = 'концепция'
db_aspects_highconcept_value = 'Здесь можно прописать концепцию персонажа.'
db_aspects_trouble = 'проблемы'
db_aspects_trouble_value = 'Проблемы вашего персонажа.'
db_aspects_first_aspect = 'Сюда можно прописать аспекты персонажа'

db_approaches = 'подходы'
db_approaches_careful = 'аккуратный'
db_approaches_clever = 'умный'
db_approaches_flashy = 'эффективный'
db_approaches_forceful = 'сильный'
db_approaches_quick = 'проворный'
db_approaches_sneaky = 'хитрый'