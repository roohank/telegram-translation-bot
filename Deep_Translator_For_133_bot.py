from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translator import translate, languages
from functions import list_to_list, key_finder, save_dict_to_json, read_json_file

# Global variables for saving user language preferences
output_directory = './data'
json_file_name = 'UsersLanguage'

app = Client("Deep_Translator_for_133_bot")

# Load previously saved user language settings from JSON file
users_lang = read_json_file(output_directory, json_file_name)
try:
    if len(users_lang) == 0:
        pass
except:
    users_lang = {}
    save_dict_to_json(users_lang, output_directory, json_file_name)
    users_lang = read_json_file(output_directory, json_file_name)

# Get the available languages and organize them into pages
langs_dict, accepted_langs, more_list_1, more_list_2, more_list_3, more_list_4, more_list_5, more_list_6 = languages()

accepted_langs.append('more 1/7')
more_list_1.append('more 2/7')
more_list_2.append('more 3/7')
more_list_3.append('more 4/7')
more_list_4.append('more 5/7')
more_list_5.append('more 6/7')
more_list_6.append('Back')

# Create the "Change Language" button
change_btn = [[InlineKeyboardButton('Change Language', callback_data='change')]]
keyboard_change = InlineKeyboardMarkup(change_btn)

# Create the main language selection keyboard
btns_page_0 = []
list_to_list(langs_dict, accepted_langs, btns_page_0, 4, 'more')
keyboard = InlineKeyboardMarkup(btns_page_0)

# Create paginated language selection keyboards
btns_page_1, btns_page_2, btns_page_3, btns_page_4, btns_page_5, btns_page_6 = [], [], [], [], [], []

list_to_list(langs_dict, more_list_1, btns_page_1, 4, 'more')
keyboard_1 = InlineKeyboardMarkup(btns_page_1)

list_to_list(langs_dict, more_list_2, btns_page_2, 4, 'more')
keyboard_2 = InlineKeyboardMarkup(btns_page_2)

list_to_list(langs_dict, more_list_3, btns_page_3, 4, 'more')
keyboard_3 = InlineKeyboardMarkup(btns_page_3)

list_to_list(langs_dict, more_list_4, btns_page_4, 4, 'more')
keyboard_4 = InlineKeyboardMarkup(btns_page_4)

list_to_list(langs_dict, more_list_5, btns_page_5, 4, 'more')
keyboard_5 = InlineKeyboardMarkup(btns_page_5)

list_to_list(langs_dict, more_list_6, btns_page_6, 4, 'back')
keyboard_6 = InlineKeyboardMarkup(btns_page_6)


@app.on_message(filters.command("start") & filters.private)
def start(client, message):
    """Send a welcome message and show language selection menu"""
    welcome_text = "Welcome! Please choose your preferred language for translation"
    message.reply(welcome_text, reply_markup=keyboard)


@app.on_callback_query()
def set_language(client, callback_query):
    """Handle user selection for target language"""
    choose_text = "Please choose your preferred language for translation"
    user_id = callback_query.from_user.id
    data = callback_query.data.lower()

    # Handle pagination
    if data == 'more 1/7':
        callback_query.message.reply(choose_text, reply_markup=keyboard_1)
    elif data == 'more 2/7':
        callback_query.message.reply(choose_text, reply_markup=keyboard_2)
    elif data == 'more 3/7':
        callback_query.message.reply(choose_text, reply_markup=keyboard_3)
    elif data == 'more 4/7':
        callback_query.message.reply(choose_text, reply_markup=keyboard_4)
    elif data == 'more 5/7':
        callback_query.message.reply(choose_text, reply_markup=keyboard_5)
    elif data == 'more 6/7':
        callback_query.message.reply(choose_text, reply_markup=keyboard_6)
    elif data == 'back':
        callback_query.message.reply(choose_text, reply_markup=keyboard)
    elif data == 'change':
        callback_query.message.reply(choose_text, reply_markup=keyboard)

    else:
        # Save the selected language for the user
        users_lang[str(user_id)] = data
        seted_lang = key_finder(langs_dict, data)
        callback_query.message.reply(f"Language set to {seted_lang}.")
        save_dict_to_json(users_lang, output_directory, json_file_name)


@app.on_message(filters.text & filters.private)
def translator(client, message):
    """Translate user messages to their selected target language"""
    users_lang = read_json_file(output_directory, json_file_name)
    user_id = message.from_user.id

    # Default target language is English
    target = users_lang.get(str(user_id), 'en')
    if target not in langs_dict.values():
        target = 'en'

    try:
        translated = translate(message.text, target=target)
        message.reply(translated, reply_markup=keyboard_change)
    except:
        message.reply('Your language was not recognized!', reply_markup=keyboard_change)


app.run()
