import requests
import json
from pprint import pprint

'''
ODataクエリによる検索(最新２０件取得)
'''

def main(url):
  r = requests.get(url)
  data = json.loads(r.text)
  pprint(data)


if __name__ == '__main__':
  url = 'https://versatileapi.herokuapp.com/api/text/all?$orderby=_created_at%20desc&$limit=20'

  main(url)
