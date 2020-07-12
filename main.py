import json

'''
1. Для каждой новости ищем в описании все слова, длина которых больше указанной в параметрах
2. Для каждого слова соответствующей длины увеличиваем счетчик упоминаний
3. После того как счетчик упоминаний по каждому слову посчитан, выбираем топ-10
'''

def update_words_rating(rating:map, text:str, word_min_length=6):
    words = text.split()
    for word in words:
        if len(word) < word_min_length:
            continue
        rating.setdefault(word, 0)
        rating[word] += 1

def words_rating_from_json_news(filename) -> map:
    words_rating = {
        # word: number_of_entries
    }
    with open(filename, encoding='utf-8') as newsfile:
        data = json.load(newsfile)

    channel_data = data['rss']['channel']
    for news_item in channel_data['items']:
        update_words_rating(words_rating, news_item['description'])

    return words_rating

def print_top10(words_rating):
    rating_list = list(words_rating.items())
    rating_list.sort(key=lambda item: item[1], reverse=True)
    for rating_item in rating_list[0:9]:
        print(rating_item[0])

words_rating = words_rating_from_json_news('newsafr.json')
print_top10(words_rating)