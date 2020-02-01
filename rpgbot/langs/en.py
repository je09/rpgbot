# commands.py
warning_game_already_exists = """This game was already started in this group.
Now invite some players, make them join with `/player <character name>`, check your characters with `/show`, adjust your character sheet with `/update`, and roll dices with `/roll`.
For a more complete list of commands, see https://github.com/simonebaracchi/rpgbot."""
warning_run_in_group = 'You must run this command in a group.'
warning_one_game = 'Sorry, only one game at a time is currently supported.'
warning_no_game_found = 'No game found.'
warning_gm_role = 'You need to be a game master to close a game.'
warning_maximum_item_number = 'You exceeded the maximum number of items. Please delete some first.'
warning_item_not_found = 'Item {}/{} not found.'
warning_not_in_game = 'You are not in a game.'
warning_no_items_found = 'No items found.'
warning_less_dices = 'Sorry, try with less dices.'
warning_invalid_dices = 'Invalid dice format.'
warning_couldnt_send_dice_result = '{}, I couldn\'t send you the roll results. Please send me a private message to allow me sending future rolls.'

question_new_container_name = 'How do you want to name the container?'
question_new_game_name = 'How are we going to call the game?'
question_template = 'Please choose a game template. This will only affect the default character sheets and dices.'
question_player_name = 'What is your name, adventurer?'
question_container = 'In which container?'
question_add_item_key = 'What item would you like to add?'
question_set_item_key = 'What would you like to set it to?'
question_which_item_key = 'Which item?'
question_which_player = 'Which player?'
question_what_to_add = 'What would you like to add?'

message_welcome_bot = """Howdy, human.
I am a character sheet bot for Fate RPG.
To use my services, add me to a group, invite other players, and call me again to start a new game.
Use the inline keyboard to navigate my character sheet functions, or use the shortcut `/roll` to roll dices.
Visit the official site for more details.

Hope you have fun!"""
message_game_created = 'New game created: {}.'
message_del_game = 'GG, humans.'
message_known_as = 'You will now be known as {}.'
message_groups_players = '{} ({})\nGroups: {}\nPlayers: {}'
message_room_aspects = '\nRoom aspects:\n{}'
message_welcome = 'Welcome, {}.'
message_updated_form = 'Updated {}/{} from {} to {} (changed {}).'
message_updated = 'Updated {}/{} to "{}".'
message_added = 'Added "{}" to container {}.'
message_deleted_item = 'Deleted {}/{} (was {}).'
message_character_sheet = 'Character sheet for {}:\n'
message_dice_rolled = 'Rolled {} = {}.'
message_gm_dice_rolled = '{} secretly rolls {}...'
message_dice_you_rolled = 'You rolled {} = {}.'
message_rolled = '{} ({}) rolled {} = {}.'
message_suggest_new_game = """Howdy, earthlings.
I am a character sheet bot for Fate RPG.
How can I help you?"""

keyboard_site = 'Go to official site ->'
keyboard_rooms_items = 'Room items'
keyboard_saved_rolls = 'Saved rolls'
keyboard_new_container = 'New container...'
keyboard_join_game = 'Join game'
keyboard_roll_dices = 'Roll dices (shortcut: /roll <dice>)'
keyboard_how_can_i_help = 'How can I help you?'
keyboard_new_game = 'Start new game'
keyboard_game_status = 'Show game status'
keyboard_player_status = 'Show player status'
keyboard_other_player_status = 'Show other player status'
keyboard_add_item = 'Add item'
keyboard_update_item = 'Update item'
keyboard_add_list_item = 'Add list item'
keyboard_delete_item = 'Delete item'
keyboard_roll_dices_gm = 'Roll dices secretly (shortcut: /gmroll)'
keyboard_cancel = 'Cancel'
keyboard_more = 'More ...'
keyboard_change_player_name = 'Change player name'
keyboard_delete_game = 'Delete game'
keyboard_back = '<- Back'


# keyboard.py
warning_too_late = 'Too late.'
no_message = '(no message)'


# db,py
db_general = 'general'
db_general_description = 'description'
db_general_description_value = 'Describe your character in a few words.'
db_general_fatepoints = 'fatepoints'
db_general_refresh = 'refresh'
db_general_stress = 'stress'
db_general_dnd_class = 'class'
db_general_dnd_class_value = 'Your class.'
db_general_race = 'race'
db_general_race_value = 'Your race.'
db_general_alignment = 'alignment'
db_general_alignment_value = 'Your alignment.'
db_general_level = 'level'
db_general_attributes = 'attributes'
db_general_attributes_strength = 'strength'
db_general_attributes_dexterity = 'dexterity'
db_general_attributes_constitution = 'constitution'
db_general_attributes_intelligence = 'intelligence'
db_general_attributes_wisdom = 'wisdom'
db_general_attributes_charisma = 'charisma'

db_inactive = 'Inactive'
db_stunts = 'stunts'
db_stunts_value = 'Set this to your first stunt.'

db_aspects = 'aspects'
db_aspects_highconcept = 'highconcept'
db_aspects_highconcept_value = 'Set this to your high concept.'
db_aspects_trouble = 'trouble'
db_aspects_trouble_value = 'Your character\'s trouble.'
db_aspects_first_aspect = 'Set this to your first aspect.'

db_approaches = 'approaches'
db_approaches_careful = 'careful'
db_approaches_clever = 'clever'
db_approaches_flashy = 'flashy'
db_approaches_forceful = 'forceful'
db_approaches_quick = 'quick'
db_approaches_sneaky = 'sneaky'