import codecs
import json

news_files  = [
  './newsfr.json', 
  './newsfr.json',
  './newsfr.json',
  './newsfr.json']

for news_file in news_files:
  print('Parse {}'.format(news_file))
  with codecs.open(news_file, encoding="iso8859_5") as data:
    rss = json.load(data)
    rss_items = rss['rss']['channel']['item']
    for rss_item in rss_items:
      words = str(rss_item['description']).split()
      print(words)