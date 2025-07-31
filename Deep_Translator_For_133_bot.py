from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translator import translate, languages
from functions import list_to_list, key_finder, save_dict_to_json, read_json_file

global output_directory
output_directory = './data'
global json_file_name
json_file_name = 'UsersLanguage'


app = Client("Deep_Translator_for_133_bot")



# ابتدا اطلاعات قبلی را از فایل JSON بخوانید
users_lang = read_json_file(output_directory, json_file_name)
try:
    if lenusers_lang == 0:
        pass
except:
    users_lang = {}
    save_dict_to_json(users_lang, output_directory, json_file_name)
    # خواندن دیکشنری از json
    users_lang = read_json_file(output_directory, json_file_name)


langs_dict, accepted_langs, more_list_1, more_list_2, more_list_3, more_list_4, more_list_5, more_list_6 = languages()

accepted_langs.append('more 1/7')
more_list_1.append('more 2/7')
more_list_2.append('more 3/7')
more_list_3.append('more 4/7')
more_list_4.append('more 5/7')
more_list_5.append('more 6/7')
more_list_6.append('Back')

#تعریف کلید تغییر زبان
change_btn = []
change_btn.append([InlineKeyboardButton('Change Language', callback_data='change')])

keyboard_change = InlineKeyboardMarkup(change_btn)


#تعریف صفحه کلید اصلی
btns_page_0 = []
list_to_list(langs_dict, accepted_langs, btns_page_0, 4, 'more')

keyboard = InlineKeyboardMarkup(btns_page_0)

#تعریف صفحه کلید 
btns_page_1 = []
list_to_list(langs_dict, more_list_1, btns_page_1, 4, 'more')

keyboard_1 = InlineKeyboardMarkup(btns_page_1)
#تعریف صفحه کلید 2
btns_page_2 = []
list_to_list(langs_dict, more_list_2, btns_page_2, 4, 'more')

keyboard_2 = InlineKeyboardMarkup(btns_page_2)
#تعریف صفحه کلید 3
btns_page_3 = []
list_to_list(langs_dict, more_list_3, btns_page_3, 4, 'more')

keyboard_3 = InlineKeyboardMarkup(btns_page_3)
#تعریف صفحه کلید 4
btns_page_4 = []
list_to_list(langs_dict, more_list_4, btns_page_4, 4, 'more')

keyboard_4 = InlineKeyboardMarkup(btns_page_4)
#تعریف صفحه کلید 5
btns_page_5 = []
list_to_list(langs_dict, more_list_5, btns_page_5, 4, 'more')

keyboard_5 = InlineKeyboardMarkup(btns_page_5)
#تعریف صفحه کلید 6
btns_page_6 = []
list_to_list(langs_dict, more_list_6, btns_page_6, 4, 'back')

keyboard_6 = InlineKeyboardMarkup(btns_page_6)

@app.on_message(filters.command("start") & filters.private)
def start(client, message):
    welcome_text = "Welcome! Please choose your preferred language for translation"
    message.reply(welcome_text, reply_markup=keyboard)

@app.on_callback_query()
def set_language(client, callback_query):
    choose_text = "Please choose your preferred language for translation"
    user_id = callback_query.from_user.id
    data = callback_query.data.lower()  # Convert data to lowercase for consistent comparison

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

        users_lang[str(user_id)] = data


        # زبان مورد نظر تنظیم شود
        seted_lang = key_finder(langs_dict, data)
        callback_query.message.reply(f"Language set to {seted_lang}.")

        save_dict_to_json(users_lang, output_directory, json_file_name)

@app.on_message(filters.text & filters.private)
def translator(client, message):
    users_lang = read_json_file(output_directory, json_file_name)


    user_id = message.from_user.id

    target = users_lang.get(str(user_id), 'en')
    if target not in langs_dict.values():
        target = 'en'


    try:
        translated = translate(message.text, target=target)
        message.reply(translated, reply_markup=keyboard_change)
    except:
        text_error = 'Your language was not recognized!'
        message.reply(text_error, reply_markup=keyboard_change)

app.run()
