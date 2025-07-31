from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os, json
def list_to_list(langs_dict, list_1, btns, lenth, word):
	row = []

	for lang_name in list_1:
		if not lang_name[:4].lower() == word:
			row.append(InlineKeyboardButton(lang_name, callback_data=langs_dict[lang_name]))
		if lang_name[:4].lower() == word:
			row.append(InlineKeyboardButton(lang_name, callback_data=lang_name))

		if len(row) == lenth:
			btns.append(row)
			row = []
	if row:
		btns.append(row)

#تابع پیدا کردن کلید از یک مقدار در دیکشنری
def key_finder(my_dict, value):
	for k, v in my_dict.items():
		if v == value:
			break

	return k
	return btns
#تابع ذخیره دیکشنری توی جیسون
def save_dict_to_json(data_dict, file_path, file_name):
    # اطمینان حاصل شود که پوشه مورد نظر برای ذخیره فایل وجود دارد
    os.makedirs(file_path, exist_ok=True)

    # ترکیب مسیر پوشه با نام فایل JSON
    json_file_path = os.path.join(file_path, file_name)

    try:
        with open(json_file_path, 'w') as file:
            json.dump(data_dict, file, indent=4)
#        print(f"Data saved successfully to {json_file_path}")
    except Exception as e:
        return f"Error: {e}"

# تابع خواندن فایل جیسون
def read_json_file(file_directory, file_name):
    # ترکیب مسیر پوشه با نام فایل JSON
    file_path = os.path.join(file_directory, file_name)

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
#        print(f"Error: File not found at {file_path}")
        return None
    except json.JSONDecodeError:
#        print(f"Error: Invalid JSON format in file at {file_path}")
        return None



if __name__ == '__main__':
	from translator import languages
	langs, accepted_langs, more_list_1, more_list_2, more_list_3, more_list_4, more_list_5, more_list_6 = languages()
	accepted_langs = ['arabic', 'english', 'french', 'german', 'hindi', 'italian', 'persian', 'russian', 'spanish', 'turkish', 'japanese', 'ukrainian', 'tajik', 'more']

	btns = []
	list_to_list(langs, accepted_langs, btns, 4, 'more')
	print(btns)