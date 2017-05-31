import codecs
import json
import re

news_files  = [
  './newsfr.json', 
  './newsfr.json',
  './newsfr.json',
  './newsfr.json']

def read_rss_items_from_file(file_name):
  with codecs.open(file_name, encoding="iso8859_5") as data:
    rss = json.load(data)
    return rss['rss']['channel']['item']


def convert_rss_items_to_words(rss_items):
  words = []
  for rss_item in rss_items:
    words.extend(re.split('\W+', str(rss_item['description'])))
  return words


def caculate_long_words_frequency(words):
  frequency_map = {}
  for word in words:
    if len(word) >= 6:
      frequency_map[word] = frequency_map.get(word, 0) + 1
  return frequency_map


def main():
  for news_file in news_files:
    print('Parse {}'.format(news_file))
    rss_items = read_rss_items_from_file(news_file)
    words = convert_rss_items_to_words(rss_items)
    frequency_map = caculate_long_words_frequency(words)
    print(frequency_map)


main()