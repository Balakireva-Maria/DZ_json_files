import json

list_for_data = []
list_for_words = []
dict_for_words = {}

with open('newsafr.json') as f:
    data = json.load(f)
    data_for_analys = (data['rss']['channel']['items'])
    for dict_ in data_for_analys:
        dict_ = (dict_['description'])
        list_for_data.append(dict_.split())

    for data in list_for_data:
        for news in data:
            list_for_words.append(news)

    for words in list_for_words:
        if len(words) > 6:
            dict_for_words[words] = (list_for_words.count(words), 'раз встречается слово')
    a = zip(dict_for_words.values(), dict_for_words.keys())
    print(sorted(list(a), reverse=True)[0:11])
