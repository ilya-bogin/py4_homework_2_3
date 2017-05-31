import codecs
import json
import re

news_files  = [
  {'file' : './newsafr.json', 'encoding' : 'KOI8-R'},
  {'file' : './newscy.json', 'encoding' : 'KOI8-R'},
  {'file' : './newsfr.json', 'encoding' : 'iso8859_5'},
  {'file' : './newsit.json', 'encoding' : 'CP1251'}]


blacklisted_words = ['country', 'votpusk', '__cdata', 'kurort']


def read_rss_items_from_file(file_name, encoding_type):
  with codecs.open(file_name, encoding=encoding_type) as data:
    rss = json.load(data)
    return rss['rss']['channel']['item']


def convert_rss_items_to_words(rss_items):
  words = []
  for rss_item in rss_items:
    words.extend(re.split('\W+', str(rss_item['description'])))
  return words


def caculate_long_words_frequency(words, blacklisted_words):
  frequency_map = {}
  for word in words:
    if len(word) >= 6 and word not in blacklisted_words:
      frequency_map[word] = frequency_map.get(word, 0) + 1
  return frequency_map


def get_top_items_from_frequency_map(frequency_map, number_of_items):
  return sorted(frequency_map, key=frequency_map.get, reverse=True)[:number_of_items]


def main():
  all_words = []
  for news_file in news_files:
    print('Parse {}'.format(news_file['file']))
    rss_items = read_rss_items_from_file(news_file['file'], news_file['encoding'])
    all_words.extend(convert_rss_items_to_words(rss_items))
  frequency_map = caculate_long_words_frequency(all_words, blacklisted_words)
  top_ten_words = get_top_items_from_frequency_map(frequency_map, 10)
  print('\nTop ten words by frequency:')
  for word in top_ten_words:
    print("{0}:{1}".format(word, frequency_map[word]))


main()