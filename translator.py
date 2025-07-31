from deep_translator import GoogleTranslator

def languages():
    langs = GoogleTranslator().get_supported_languages(as_dict= True)
    supported_languages_google = GoogleTranslator().get_supported_languages()
    accepted_langs = ['arabic', 'english', 'french','german','hindi','italian','persian','russian','spanish','turkish', 'japanese', 'tajik', 'ukrainian']
    more_list_1 = []
    more_list_2 = []
    more_list_3 = []
    more_list_4 = []
    more_list_5 = []
    more_list_6 = []

    for i in range(0, 6):
        l = 0
        for lang in  supported_languages_google:
            if not lang in accepted_langs and not lang in more_list_1 and not lang in more_list_2 and not lang in more_list_3 and not lang in more_list_4 and not lang in more_list_5 and not lang in more_list_6:
                if i == 0:
                    more_list_1.append(lang)
                if i == 1:
                    more_list_2.append(lang)
                if i == 2:
                    more_list_3.append(lang)
                if i == 3:
                    more_list_4.append(lang)
                if i == 4:
                    more_list_5.append(lang)
                if i == 5:
                    more_list_6.append(lang)
                l += 1
                if l == 20:
                    break

    return langs, accepted_langs, more_list_1, more_list_2, more_list_3, more_list_4, more_list_5, more_list_6

def translate(text, target, source='auto'):
    return GoogleTranslator(source=source, target=target).translate(text)
    

if __name__ == '__main__':
    text = 'سلام عزیزم , خوبی؟'
    source = 'fa'
    target = 'de'
    print(translate(text, target))
